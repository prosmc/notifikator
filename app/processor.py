 # -*- coding: utf-8 -*-

import sys
import time
import threading
from datetime import datetime
from elasticsearch import Elasticsearch
from flask import current_app
from .client import ClientFactory, ClientType
from .utils import Timer, TimeStamp, IndexName
from .template import TemplateHandler

class Processor():

    def __init__(self, *args, **kwargs):
        self.app = kwargs.get('app', None)
        self.app.logger.debug("Processor is initialized.")
        self.name = kwargs.get('name', None)
        self.config = kwargs.get('config', None)
        self.timestamp = TimeStamp.format()
        self.index_01 = IndexName.format(self.config['APP_ES_INDEX_01'])
        self.index_02 = IndexName.format(self.config['APP_ES_INDEX_02'])
        self.timer = Timer()

    def get_query_result(self):
        template_handler = TemplateHandler(template_path="templates/elasticsearch/queries")
        name = self.config["APP_ES_INDEX_01"]
        template_param = name + ""
        index = self.es_client.search_template(index=name, body=template_handler.get_data('aggs_query.json.j2', template_id=template_param))
        index_correlation_keys = [ correlation_key['key'] for correlation_key in index['aggregations']['correlation_key']['buckets'] ]
        return index_correlation_keys
        
    def notify(self):
        with self.app.app_context():
            current_app.logger.debug(f"Notifikator is running ...")
  
    def run(self):
        self.timer.set_start_time()
        with self.app.app_context():
            try:
                self.es_client = ClientFactory.newInstance(ClientType.ELASTICSEARCH, self.app)
                self.notify()
                current_app.logger.info(f"Elapsed Time (sec.): { self.timer.get_run_time() }")
                self.es_client.transport.close()
            except Exception as other:
                current_app.logger.error(f"Processor run exception occured: {other}")