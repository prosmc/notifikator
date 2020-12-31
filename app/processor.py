 # -*- coding: utf-8 -*-

import sys
import time
import threading
from datetime import datetime
from enum import Enum
from elasticsearch import Elasticsearch
from flask import current_app
from .client import ClientFactory, ClientType
from .utils import Timer, TimeStamp, IndexName
from .template import TemplateHandler
from .adapters.handler import AdapterHandler

class ProcessorType(Enum):
    TYPE_01 = 'publisher'
    TYPE_02 = 'subscriber'

class Processor():

    def __init__(self, *args, **kwargs):
        self.app = kwargs.get('app', None)
        self.app.logger.debug("Processor is initialized.")
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.config = kwargs.get('config', None)
        self.timestamp = TimeStamp.format()
        self.index_01 = IndexName.format(self.config['APP_ES_INDEX_01'])
        self.index_02 = IndexName.format(self.config['APP_ES_INDEX_02'])
        self.adapter_handler = AdapterHandler(self.app)
        self.timer = Timer()

    def get_search_query_result(self):
        with self.app.app_context():
            app_id = self.app.config['APP_ID']
            index_name = self.config['APP_ES_INDEX_01']
            template_handler = TemplateHandler(template_path="templates/elasticsearch/queries")
            template_id = app_id + "-" + index_name + "-" + "query"
            response = self.es_client.search_template(index=index_name, body=template_handler.get_data('query_01.json.j2', template_id=template_id))
            return response
        
    def execute(self):
        with self.app.app_context():
            documents = self.get_search_query_result()
            for num, doc in enumerate(documents['hits']['hits']):
                current_app.logger.debug(f"Document found - id: { doc['_id'] }")
                if (self.type == ProcessorType.TYPE_01.value):
                    self.adapter_handler.run_publisher_adapters(json_data=doc)
                if (self.type == ProcessorType.TYPE_02.value):
                    self.adapter_handler.run_subscriber_adapters(json_data=doc)
                
    def run(self):
        self.timer.set_start_time()
        with self.app.app_context():
            try:
                self.es_client = ClientFactory.newInstance(ClientType.ELASTICSEARCH, self.app)
                self.execute()
                current_app.logger.info(f"Elapsed Time (sec.): { self.timer.get_run_time() }")
                self.es_client.transport.close()
            except Exception as other:
                current_app.logger.error(f"Processor run exception occured: {other}")