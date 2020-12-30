 # -*- coding: utf-8 -*-

class Adapter:

    def __init__(self, app, adapter):
        self.app      = app
        self.adapter  = adapter

    def send(self, json_data):
        self.adapter.send(json_data)
    
    def request(self, json_data):
        self.adapter.request(json_data)

    def __str__(self):
        return str(self.obj)
