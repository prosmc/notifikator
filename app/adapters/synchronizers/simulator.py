 # -*- coding: utf-8 -*-

from app.utils import Timer, TimeStamp
from app.client import ClientFactory, ClientType
from app.queries.query import QueryHandler
from flask import current_app
import json
import uuid

class SimulatorAdapter():

    def __init__(self, app, name):
        self.app      = app
        self.name     = name
        self.client   = ClientFactory.newInstance(ClientType.ELASTICSEARCH, self.app)
        self.index_01 = self.app.config['APP_ES_INDEX_01']
        self.index_02 = self.app.config['APP_ES_INDEX_02']

    def read(self, json_data):
        with self.app.app_context():
            app_id           = self.app.config['APP_ID']
            client           = self.es_client
            index_name       = self.config['APP_ES_INDEX_02']
            template_path    = 'templates/elasticsearch/queries'
            template_file    = 'query_01.json.j2'
            template_handler = TemplateHandler(template_path=template_path)
            template_id      = app_id + "-" + "query-01"
            incident_id      = doc = json_data['_source']['incident.id']
            query_handler    = QueryHandler(self.app)

            hits = query_handler.get_search_query_result(
                app_id=app_id,
                client=client,
                index_name=index_name,
                template_path=template_path,
                template_file=template_file,
                template_handler=template_handler,
                template_id=template_id,
                incident_id=incident_id
            )
            return hits

    def update(self, json_data, documents):
        with self.app.app_context():
            for num, doc in enumerate(documents['hits']['hits']):
                current_app.logger.debug(f"Document found - id: { doc['_id'] }")
                source_to_update = {
                    "doc" : {
                        "state" : doc['_source']['state']
                    }
                }
            
                current_app.logger.debug(f"update set state={ doc['_source']['state'] } for incident with id={ json_data['_id'] }")
                response = self.client.update(
                    index=self.index_01,
                    doc_type='_doc',
                    id=json_data['_id'],
                    refresh=True,
                    body=source_to_update
                )

    def run(self, json_data):
        with self.app.app_context():
            current_app.logger.debug(f"Subscriber Simulator Adatpter is running ...")
            hits = read(json_data)
            #update(json_data, hits)

    def __str__(self):
        return f"Sync Adapter Name: { self.name }"