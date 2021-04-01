# -*- coding: utf-8 -*-

from multiprocessing import shared_memory

class Building(object):
        
    def __init__(self, buildingName="null_name"):
        self.buildingName = buildingName
        self.tupleSpace = shared_memory.ShareableList()
                
    def processFireAlarmEvent(self):
        print("Fire alarm event received in building "+ self.buildingName)
        
    
        
    
        
    