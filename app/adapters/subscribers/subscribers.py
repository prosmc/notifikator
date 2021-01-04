 # -*- coding: utf-8 -*-

class SubsriberAdapter:

    def __init__(self, app, adapter):
        self.app      = app
        self.adapter  = adapter

    def subscribe(self, json_data):
        self.adapter.subscribe(json_data)
    
    def __str__(self):
        return str(self.obj)
