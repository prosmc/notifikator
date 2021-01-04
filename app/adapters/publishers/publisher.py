 # -*- coding: utf-8 -*-

class PublisherAdapter:

    def __init__(self, app, adapter):
        self.app      = app
        self.adapter  = adapter

    def publish(self, json_data):
        self.adapter.publish(json_data)
    
    def __str__(self):
        return str(self.obj)
