# -*- coding: utf-8 -*-

#from multiprocessing import Manager
import memcache

class Building(object):        
    
    #when using non default port, make sure the service setting is changed
    def __init__(self, buildingName="default_name", port=11211, debug=0):
        
        self.buildingName = buildingName
        self.debug = debug == 1
                
        address = '127.0.0.1:'+str(port)
        self.sharedMemory = memcache.Client([address], debug=debug)

                
    def processFireAlarmEvent(self):
        print("Fire alarm event received in building "+ self.buildingName)
        
        
    #Procedure to change the status of an employee based on their ID to 
    #currently inside the building
    def processPersonelEnteringEvent(self, personelId):
        #read the tuple
        t = self.sharedMemory.get(personelId)
        
        if self.debug:
            print("personel entering " + personelId + " " + t)
        
        #modify the tuple's status field
        t["status"] = "CURRENTLY INSIDE"

        #write the tuple
        self.sharedMemory.set(personelId, t)

    #Procedure to change the status of an employee based on their ID to 
    #authorized after leaving the building        
    def processPersonelLeavingEvent(self, personelId):
        #read the tuple
        t = self.sharedMemory.get(personelId)
        
        if self.debug:
            print("personel entering "+personelId + " " + t)
        
        #modify the tuple's status field
        t["status"] = "AUTHORIZED"

        #write the tuple
        self.sharedMemory.set(personelId, t)
        
    
if __name__ == '__main__':
    b = Building("8C - Chartreuse")
        
    