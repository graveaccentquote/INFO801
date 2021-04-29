# -*- coding: utf-8 -*-
import memcache
from multiprocessing import Process
from pymitter import EventEmitter

from fireAlarm import FireAlarm


class Building(object):        
    
    #when using non default port, make sure the service setting is changed
    def __init__(self,
                 fireAlarmKey,
                 name="default_name",
                 memCacheAddress='127.0.0.1:11211',
                 debug=0):

        self.name = name
        
        #shared memory        
        self.sharedMemory = memcache.Client([memCacheAddress], debug=debug)
        
        #fire alarm event emitter/handler
        self.ee = EventEmitter()
        fireAlarm = FireAlarm(fireAlarmKey, self.ee)
        self.ee.on("fireAlarmEvent", self.handleFireAlarmEvent)
        fireAlarmProcess = Process(target=fireAlarm.listenKB)
        fireAlarmProcess.start()
        
        
    def handleFireAlarmEvent(self):
        print ("Received Fire Alarm in building "+ self.name)
        
        #updating locations
        idList = self.sharedMemory.get("idList")

        for pId in idList:
            personel = self.sharedMemory.get(pId)
            
            if self.name == personel['location']:
                personel['location'] = "outside"
        
    
if __name__ == '__main__':
    chartreuse  = Building('m', "8C - Chartreuse")
    pm          = Building('p', "3 - Pôle Montagne", debug=1)
        
    