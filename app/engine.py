 # -*- coding: utf-8 -*-

import os
import sys
import threading
import time

class Engine(threading.Thread):

    def __init__(self, target, name, processor, interval):
        super(Engine, self).__init__(target=target,name=name)
        self._stop = threading.Event()
        self.processor = processor
        self.interval = interval

    def run(self):
        while not self._stop.is_set():
            self.processor.run()
            time.sleep(self.interval)

    def stop(self):
        self._stop.set()
        
    def stopped (self):
        return self._stop.isSet()

    @staticmethod
    def get_thread_by_name(name):
        threads = threading.enumerate()
        for thread in threads:
            if thread.getName () == name:
                return thread
        return None