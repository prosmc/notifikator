 # -*- coding: utf-8 -*-

class Adapter:

    def __init__(self, app, adapter):
        self.app                = app
        self.adapter_instance   = adapter

    def run(self, json_data):
        self.adapter_instance.run(json_data)
    
    def __str__(self):
        return str(self.obj)
