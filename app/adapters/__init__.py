 # -*- coding: utf-8 -*-

class Adapter:

    def __init__(self, name, app):
        self.name = name
        self.app  = app
        self.index_01 = self.app.config['APP_ES_INDEX_01']
        self.index_02 = self.app.config['APP_ES_INDEX_02']

    def execute(self, json_data):
        pass
        
    def __str__(self):
        return str(self.obj)
