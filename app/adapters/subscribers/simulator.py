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

    #TODO: Method must be implemented.
    def filter(self, json_data):
        pass

    #TODO: Method must be implemented.
    def get_search_query_result(self):
        pass

    #TODO: Method must be implemented.
    def read(self, json_data):
        pass

    #TODO: Method must be implemented.
    def update(self, json_data):
        pass

    #TODO: Method must be implemented.
    def subscribe(self, json_data):
        with self.app.app_context():
            current_app.logger.debug(f"Subscriber Simulator Adatpter is running ...")

    def __str__(self):
        return f"Sender Adapter Name: { self.name }"