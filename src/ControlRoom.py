# -*- coding: utf-8 -*-

from multiprocessing import shared_memory

from building import Building

class ControlRoom(object):
    
    def __init__(self):
        self.buildingMap = {}
        
    def addBuilding(self, building):
        self.buildingMap[building.name] = building
     
        
    # takes a building name as parameter, polls the list of personel currently
    # in that building by reading the shared_memory (tuple space) attached to
    # said building.
    def pollCurrentlyInPersonel(self, buildingName):
        #self.buildingMap[buildingName].tupleSpace.shm.name
        #TODO
        print()
        
        

