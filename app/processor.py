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
from .queries.query import QueryHandler

class ProcessorType(Enum):
    TYPE_01 = 'publisher'
    TYPE_02 = 'subscriber'

class Processor():

    def __init__(self, *args, **kwargs):
        self.app = kwargs.get('app', None)
        self.app_id = self.app.config['APP_ID']
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.config = kwargs.get('config', None)
        self.template_path = kwargs.get('template_path', None)
        self.template_file = kwargs.get('template_file', None)
        self.query_name = kwargs.get('query_name', None)
        self.template_id = self.app_id + "-" + self.query_name
        self.incident_id = kwargs.get('incident_id', None)
        self.state = kwargs.get('state', None)
        self.index_name = kwargs.get('index_name', None)
        self.timestamp = TimeStamp.format()
        self.index_01 = IndexName.format(self.config['APP_ES_INDEX_01'])
        self.index_02 = IndexName.format(self.config['APP_ES_INDEX_02'])
        self.adapter_handler = AdapterHandler(self.app)
        self.query_handler = QueryHandler(self.app)
        self.timer = Timer()
        self.app.logger.debug("Processor is initialized.")
       
    def execute(self, **kwargs):
        with self.app.app_context():
            documents = self.query_handler.get_search_query_result(
                app_id=self.app_id,
                client=self.client,
                index_name=self.index_name,
                template_path=self.template_path,
                template_file=self.template_file,
                template_id=self.template_id,
                incident_id=self.incident_id,
                state=self.state
            )

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
                self.client = ClientFactory.newInstance(ClientType.ELASTICSEARCH, self.app)
                self.execute()
                current_app.logger.info(f"{ self.type.title() }-Processor Elapsed Time (sec.): { self.timer.get_run_time() }")
                self.client.transport.close()
            except Exception as other:
                current_app.logger.error(f"{ self.type.title() }-Processor run exception occured: {other}")