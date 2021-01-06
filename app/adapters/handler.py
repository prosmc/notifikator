 # -*- coding: utf-8 -*-

from .adapter import Adapter
from .publishers.simulator import SimulatorAdapter as PubSimAdp
from .synchronizers.simulator import SimulatorAdapter as SyncSimAdp
from flask import current_app
from ..processor_type import ProcessorType
class AdapterHandler():

    def __init__(self, app):
        self.app = app
        self.pub_adapters= [PubSimAdp(self.app,"simulator")]
        self.sync_adapters= [SyncSimAdp(self.app,"simulator")]

    def activate(self, json_data, adapters):
        with self.app.app_context():
            for adapter in adapters:
                current_app.logger.debug("Adapter { adapter.name } is executed.")
                adapter_instance = Adapter(self.app, adapter)
                adapter_instance.run(json_data)

    def run(self, processor_type, json_data):
        if (processor_type == ProcessorType.TYPE_01.value):
            self.activate(json_data=json_data, adapters=self.pub_adapters)
        #if (processor_type == ProcessorType.TYPE_02.value):
        #    self.adapter_handler.run_synchronizer_adapters(json_data=doc, adapters=self.sync_adapters)