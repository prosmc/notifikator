 # -*- coding: utf-8 -*-

from .publishers.publisher import PublisherAdapter
from .publishers.simulator import SimulatorAdapter as PubSimAdp
from .subscribers.simulator import SimulatorAdapter as SubSimAdp
from flask import current_app

class AdapterHandler():

    def __init__(self, app):
        self.app = app
        self.publisher_adapters= [PubSimAdp(self.app,"simulator")]

    def run_publisher_adapters(self, json_data):
        with self.app.app_context():
            for adapter in self.publisher_adapters:
                current_app.logger.debug("Publisher Adapter { adapter.name } is executed.")
                adapter_instance = PublisherAdapter(self.app, adapter)
                adapter_instance.publish(json_data)

    def run_subscriber_adapters(self, json_data):
        #TODO: Implementation of the subscriber_adapters!!!
        pass