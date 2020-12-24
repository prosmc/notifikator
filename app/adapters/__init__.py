 # -*- coding: utf-8 -*-
 
 class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)
        
    def __str__(self):
        return str(self.obj)
