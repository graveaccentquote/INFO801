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
        self.memCacheAddress = memCacheAddress
        self.debug = debug
        
        #fire alarm event emitter/handler
        ee = EventEmitter()
        fireAlarm = FireAlarm(fireAlarmKey, ee)
        ee.on("fireAlarmEvent", self.handleFireAlarmEvent)
        fireAlarmProcess = Process(target=fireAlarm.listenKB)
        fireAlarmProcess.start()
        
        
    def handleFireAlarmEvent(self):
        print ("Received Fire Alarm in building "+ self.name)
                                
        #updating locations
        mem = memcache.Client([self.memCacheAddress], debug=self.debug)
        
        idList = mem.get("idList")

        for pId in idList:
            personel = mem.get(pId)
            
            if self.name == personel['location']:
                personel['location'] = "outside"
                mem.set(pId, personel)
        
    
if __name__ == '__main__':
    chartreuse  = Building('m', "8C - Chartreuse")
    pm          = Building('p', "3 - Pôle Montagne", debug=1)
        
    