# -*- coding: utf-8 -*-

from multiprocessing import Manager

class Building(object):
        
    def __init__(self, buildingName="null_name"):
        self.buildingName = buildingName
        self.manager = Manager()
        self.dictionary = self.manager.dict()
                
    def processFireAlarmEvent(self):
        print("Fire alarm event received in building "+ self.buildingName)
        
        
    def processPersonelEnteringEvent(self, personelId):
        self.currentPersonel[personelId] = "currentlyIn"
        
    def processPersonelLeavingEvent(self, personelId):
        self.currentPersonel[personelId] = "authorized"
        
    def addAccess(self, personelId):
        self.currentPersonel[personelId] = "authorized"
    
    def removeAccess(self, personelId):
        del self.currentPersonel[personelId]
        
    def checkAccess(self, personelId):
        return personelId in self.dictionary

        
    
        
    
        
    