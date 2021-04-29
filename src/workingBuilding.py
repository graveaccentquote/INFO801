# -*- coding: utf-8 -*-

#from multiprocessing import Manager
from fireAlarm import FireAlarm
from multiprocessing import Process
import memcache
from pymitter import EventEmitter

class Building(object):        
    
    #when using non default port, make sure the service setting is changed
    def __init__(self,
                 fireAlarmKey,
                 name="default_name",
                 port=11211,
                 debug=0):
        
        self.name = name
        
        #fire alarm event emitter/handler
        self.ee = EventEmitter()
        
        self.fireAlarm = FireAlarm(fireAlarmKey, self.ee)
        self.ee.on("fireAlarmEvent", self.handleFireAlarmEvent)
            
        self.fireAlarmProcess = Process(target=self.fireAlarm.listenKB,
                                        args=())
        
        self.fireAlarmProcess.start()

        #shared memory        
        address = '127.0.0.1:'+str(port)
        self.sharedMemory = memcache.Client([address], debug=debug)
        
        #to see full debug logs
        self.debug = debug == 1
                
    def processFireAlarmEvent(self):
        print("Fire alarm event received in building "+ self.name)        
        
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
        
        
    def handleFireAlarmEvent(self):
        print ("Received Alarm in building "+ self.name)
        
        print(self.sharedMemory)
        
    
if __name__ == '__main__':
    b = Building('q', "8C - Chartreuse")
    b2 = Building('s', "test")
        
    