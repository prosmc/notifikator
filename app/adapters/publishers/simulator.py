 # -*- coding: utf-8 -*-

from app.utils import Timer, TimeStamp
from app.client import ClientFactory, ClientType
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

    def filter(self, json_data):
        with self.app.app_context():
            self.imticket_id =  "IM" + str(uuid.uuid4()).split("-")[0]
            doc = json_data['_source']
            doc["@timestamp"] = TimeStamp.format()
            doc["incident.id"] = self.imticket_id
            doc["state"] = 0
            current_app.logger.info(f"data: {doc}")
            return doc

    def create(self, json_data):
        with self.app.app_context():
            response = self.client.index(index=self.index_02, body=json_data)

    def update(self, json_data):
        with self.app.app_context():

            source_to_update = {
                "doc" : {
                    "processed" : 1,
                    "incident.id": self.imticket_id
                }
            }
            
            current_app.logger.debug(f"update set incident.id={ self.imticket_id } for incident with id={ json_data['_id'] }")
            response = self.client.update(
                index=self.index_01,
                doc_type='_doc',
                id=json_data['_id'],
                body=source_to_update
            )

    def publish(self, json_data):
        with self.app.app_context():
            current_app.logger.debug(f"Publisher Simulator Adatpter is running ...")
            self.create(self.filter(json_data))
            self.update(json_data)

    def __str__(self):
        return f"Publisher Adapter Name: { self.name }"