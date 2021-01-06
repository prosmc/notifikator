# -*- coding: utf-8 -*-

from .legend import Legend
from .utils import TimeStamp
from flask import current_app
from .engine import Engine
from .processor import ProcessorType
from .processor import Processor
from .logger import Logger
from .client import ClientType, ClientFactory
from .artifact import Artifact
from .utils import IndexName
from .template import TemplateHandler
from .artifact import Artifact
from requests.auth import HTTPBasicAuth
import requests
import time
import json

class Bootstrap:

    def __init__(self, app):
        self.app = app
        self.timestamp = TimeStamp.format()
        self.artifact = Artifact(app)

    def list_legend(self):
        Legend.show(self.app.config['APP_RELEASE'], self.timestamp)

    def list_config(self):
        with self.app.app_context():
            current_app.logger.debug("APP CONFIG")
            for key, val in self.app.config.items():
                current_app.logger.debug(f"{key}: {val}")

    def check_es_connection(self):
        client = ClientFactory.newInstance(ClientType.ELASTICSEARCH, self.app)
        retry = True
        counter = 0
        while retry and counter <= int(self.app.config['APP_ES_BOOTSTRAP_RETRY_MAX']) :
            try:
                client.cluster.health()
                current_app.logger.info("Elasticsearch connection can be established.")                   
                retry = False
            except Exception as other:
                current_app.logger.error("Elasticsearch connection can't be established.")
                counter += 1
            time.sleep(int(self.app.config['APP_ES_BOOTSTRAP_RETRY_INTERVAL']))

    def check_kb_connection(self):
        client = ClientFactory.newInstance(ClientType.KIBANA, self.app)
        retry = True
        counter = 0
        while retry and counter <= int(self.app.config['APP_KB_BOOTSTRAP_RETRY_MAX']) :
            try:
                REQUEST_URL=f"https://{self.app.config['APP_KB_HOST']}:{self.app.config['APP_KB_PORT']}/api/status"
                client.perform_request(
                    method='GET',
                    url=REQUEST_URL, 
                    auth=HTTPBasicAuth(self.app.config['APP_KB_USER'], self.app.config['APP_KB_PASSWORD']),
                    files=None, 
                    headers=None,
                    verify=eval(self.app.config['APP_KB_VERIFY_CERTS'])
                )            
                current_app.logger.info("Kibana connection can be established.")                   
                retry = False
            except Exception as other:
                current_app.logger.error("Kibana connection can't be established.")
                counter += 1
            time.sleep(int(self.app.config['APP_KB_BOOTSTRAP_RETRY_INTERVAL']))
   
    def init_logger(self):
        with self.app.app_context():
            if eval(self.app.config['APP_FLASK_LOGGER']):
                logger = Logger()
                logger.init_app(self.app)
                current_app.logger.debug(f"Flask Logger is active.")

    def create_index_ilm_policies(self):
        with self.app.app_context():
            app_id = self.app.config['APP_ID']
            es_client = ClientFactory.newInstance(ClientType.ELASTICSEARCH, self.app)
            template_handler = TemplateHandler(template_path="templates/elasticsearch/ilm")
            templates = self.app.config['APP_ILM_POLICY_TEMPLATES']
            for key, val in templates.items():
                data = template_handler.get_data(val)
                self.artifact.create_index_ilm_policy(es_client, app_id + "-" + key + "-policy", data)
                self.artifact.exists_index_ilm_policy(es_client, app_id + "-" + key + "-policy")
            es_client.transport.close()

    def create_index_templates(self):
        with self.app.app_context():
            app_id = self.app.config['APP_ID']
            es_client = ClientFactory.newInstance(ClientType.ELASTICSEARCH, self.app)
            template_handler = TemplateHandler(template_path="templates/elasticsearch/ilm")
            templates = self.app.config['APP_INDEX_TEMPLATES']
            for key, val in templates.items():
                data = template_handler.get_data(val, name=key, policy_name=app_id + "-" + key + "-policy")
                current_app.logger.debug(data)
                self.artifact.create_index_template(es_client, app_id + "-" + key + "-template", data)
            es_client.transport.close()  
                    
    def create_indices(self):
        with self.app.app_context():
            es_client = ClientFactory.newInstance(ClientType.ELASTICSEARCH, self.app)
            template_handler = TemplateHandler(template_path="templates/elasticsearch/ilm")
            templates = self.app.config['APP_INDICES']
            for key, val in templates.items():
                data = template_handler.get_data(val, name=key)    
                current_app.logger.debug(data)
                self.artifact.create_index(es_client, key, data)
            es_client.transport.close()

    def create_search_templates(self):
        with self.app.app_context():
            app_id = self.app.config['APP_ID']
            url_client = ClientFactory.newInstance(ClientType.URLLIB3HTTPCONNECTION, self.app)
            template_handler = TemplateHandler(template_path="templates/elasticsearch/scripts")
            for query_name, config_item in self.app.config['APP_INDEX_QUERIES'].items():
                data = template_handler.get_data(config_item['script_template_file'])
                current_app.logger.debug(data)
                query_name = app_id + "-" + query_name# i.e. nk01-query-01
                self.artifact.create_search_template(url_client, "post".upper(), query_name, data) 
    
    def create_index_pattern(self):
        with self.app.app_context():
            index_pattern_names = [
                self.app.config['APP_ES_INDEX_02']
            ]
            kb_client = ClientFactory.newInstance(ClientType.KIBANA, self.app)
            template_handler = TemplateHandler(template_path="templates/kibana/index_pattern")
            for index_pattern_name in index_pattern_names:
                REQUEST_URL=f"https://{self.app.config['APP_KB_HOST']}:{self.app.config['APP_KB_PORT']}/api/saved_objects/index-pattern/{index_pattern_name}"
                data = template_handler.get_data("pattern_01.json.j2", name=f"{index_pattern_name}*")
                self.artifact.create_index_pattern(client=kb_client, url=REQUEST_URL, data=data, name=f"{index_pattern_name}*")

    def create_dashboards(self):
        with self.app.app_context():
            kb_client = ClientFactory.newInstance(ClientType.KIBANA, self.app)
            template_handler = TemplateHandler(app=self.app)
            KB_DASHBOARD_FILE = self.app.config['APP_KB_TEMPLATE_FOLDER'] + '/dashboard/notifikator.ndjson.j2'
            current_app.logger.info("KB_DASHBOARD_FILE: " + KB_DASHBOARD_FILE)
            data = template_handler.get_raw_data(KB_DASHBOARD_FILE)
            current_app.logger.info(data)
            self.artifact.create_dashboard(kb_client, data)

    #def startup_engine(self):
    #    with self.app.app_context():
    #        publisher_processor = Processor(name=self.app.config['APP_NAME'] + "-Publisher-Processor", app=self.app, type=ProcessorType.TYPE_01.value, config=self.app.config)
    #        subscriber_processor = Processor(name=self.app.config['APP_NAME'] + "-Subscriber-Processor", app=self.app, type=ProcessorType.TYPE_02.value, config=self.app.config)
    #        if not Engine.get_thread_by_name(publisher_processor.name):
    #            th = Engine(target=Engine, name=self.app.config['APP_ID'] + "-Publisher-Engine", processor=publisher_processor, interval=int(self.app.config['APP_PUBLISHER_SLEEP_TIME']))
    #            th.start()
    #        if not Engine.get_thread_by_name(subscriber_processor.name):
    #            th = Engine(target=Engine, name=self.app.config['APP_ID'] + "-Subscriber-Engine", processor=subscriber_processor, interval=int(self.app.config['APP_SUBSCRIBER_SLEEP_TIME']))
    #            th.start()

    def startup_engine(self):
        with self.app.app_context():

            publisher_processor  = Processor(name=self.app.config['APP_NAME'] + "-Publisher-Processor", 
                                            app=self.app, 
                                            type=ProcessorType.TYPE_01.value, 
                                            config=self.app.config,
                                            index_name=self.app.config['APP_ES_INDEX_01'],
                                            template_path=self.app.config['APP_INDEX_QUERIES']['query-01']['template_path'] + '/queries',
                                            template_file=self.app.config['APP_INDEX_QUERIES']['query-01']['query_template_file'],
                                            query_name=list(self.app.config['APP_INDEX_QUERIES'].keys())[0],
                                            incident_id=0,
                                            state=2)

            if not Engine.get_thread_by_name(publisher_processor.name):
                th = Engine(target=Engine, name=self.app.config['APP_ID'] + "-Publisher-Engine", processor=publisher_processor, interval=int(self.app.config['APP_PUBLISHER_SLEEP_TIME']))
                th.start()

            subscriber_processor = Processor(name=self.app.config['APP_NAME'] + "-Subscriber-Processor", 
                                            app=self.app, 
                                            type=ProcessorType.TYPE_02.value, 
                                            config=self.app.config,
                                            index_name=self.app.config['APP_ES_INDEX_01'],
                                            template_path=self.app.config['APP_INDEX_QUERIES']['query-02']['template_path'] + '/queries',
                                            template_file=self.app.config['APP_INDEX_QUERIES']['query-02']['query_template_file'],
                                            query_name=list(self.app.config['APP_INDEX_QUERIES'].keys())[1],
                                            incident_id=0,
                                            state=2)

            if not Engine.get_thread_by_name(subscriber_processor.name):
                th = Engine(target=Engine, name=self.app.config['APP_ID'] + "-Subscriber-Engine", processor=subscriber_processor, interval=int(self.app.config['APP_SUBSCRIBER_SLEEP_TIME']))
                th.start()


    def set_startup_time(self):
        self.app.config['APP_STARTUP_TIME']= self.timestamp

    def startup(self):
        with self.app.app_context():
            self.init_logger()
            self.check_es_connection()
            self.check_kb_connection()
            self.list_legend()
            self.list_config()
            self.create_index_ilm_policies()
            self.create_index_templates()
            self.create_indices()
            self.create_search_templates()
            #self.create_index_pattern()
            self.create_dashboards()
            self.startup_engine()
            self.set_startup_time()

    def shutdown(self):
        pass