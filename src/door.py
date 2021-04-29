# -*- coding: utf-8 -*-

import memcache
import time
import keyboard


class Door(object):
    
    def __init__(self,
                 name,
                 parentBuildingName,
                 sensorQueue,
                 timeout=5,
                 memCacheAddress='127.0.0.1:11211',
                 debug=0):
    
        self.locked = True
        self.timeout = timeout
        self.name = name
        self.parentBuildingName = parentBuildingName
        
        #sensor
        self.sensorQueue = sensorQueue
                
        #shared memory
        self.sharedMemory = memcache.Client([memCacheAddress], debug=debug)
                        
    def processPersonelEnteringEvent(self, personelId):
        #read the tuple
        p = self.sharedMemory.get(personelId)
        
        #check if authorized
        if self.parentBuildingName not in p['auth']:
            print("BUILDING : " 
                  + self.parentBuildingName 
                  + " - Personel tried to enter without authorizations : " 
                  + p['name'])
            return
    
    
        if p['location'] != "outside":
            print("Error trying to enter building when not outside")
            return 
        
        #open the door for 5 seconds
        print("BUILDING : " + self.parentBuildingName + " Opening door (entering): " + self.name)
        
        self.locked = False
        
        
        while not self.sensorQueue.empty():
            self.sensorQueue.get() 
            
        t = time.time()
        count = 0
        
        while((time.time() - t ) < self.timeout):
            if (not self.sensorQueue.empty()):
                if count == 0:
                    #empty the queue
                    self.sensorQueue.get(block=False)
                    
                    count += 1
                    
                    print("BUILDING : " 
                          + self.parentBuildingName 
                          + " - Personel entering : " 
                          + p['name'])
                    
                    #update the tuple
                    p['location'] = self.parentBuildingName
                    self.sharedMemory.set(personelId, p)
                else:
                    print("Detected more than 1 person, triggering Alarm")
                    break
                
        print("BUILDING : " 
              + self.parentBuildingName 
              + " closing door : " 
              + self.name)
        
        self.locked = True

        
    #return true if personel is allowed in    
    def checkIfAuthorized(self, personelId):
        #read the tuple
        p = self.sharedMemory.get(personelId)
      
        return self.parentBuildingName in p['auth']
    
    def processPersonelLeavingEvent(self, personelId):
        #read the tuple
        p = self.sharedMemory.get(personelId)
        
        if p['location'] != self.parentBuildingName:
            print("Error, trying to leave building when not inside")
            return
        
        print("BUILDING : " 
              + self.parentBuildingName 
              + " - Personel leaving : " 
              + p['name'])
        
        #open the door for 5 seconds
        print("BUILDING : " 
              + self.parentBuildingName 
              + " Opening door (exiting): " 
              + self.name)
        
        self.locked = False
        
        while not self.sensorQueue.empty():
            self.sensorQueue.get() 
            
        t = time.time()
        count = 0
    
        while((time.time() - t ) < self.timeout):
            if (not self.sensorQueue.empty()):
                if count == 0:
                    #empty the queue
                    self.sensorQueue.get(block=False)
                    
                    count += 1
                    
                    print("BUILDING : " 
                          + self.parentBuildingName 
                          + " - Personel leaving : " 
                          + p['name'])
                    
                    #update the tuple
                    p['location'] = "outside"
                    self.sharedMemory.set(personelId, p)
                else:
                    print("Detected more than 1 person, triggering Alarm")
                    break
                
        print("BUILDING : " 
              + self.parentBuildingName 
              + " closing door : " 
              + self.name)
        
        self.locked = True
        
    def handleFireAlarmEvent(self):
        print("Fire Alarm event received, unlocking")
        self.locked = False
        
        
    def listenKeyboard(self):
        keyboard.add_hotkey('z', self.processPersonelEnteringEvent, args=("1"))
        keyboard.add_hotkey('s', self.processPersonelLeavingEvent,  args=("1"))
        keyboard.add_hotkey('e', self.processPersonelEnteringEvent, args=("2"))
        keyboard.add_hotkey('d', self.processPersonelLeavingEvent,  args=("2"))
        keyboard.add_hotkey('r', self.processPersonelEnteringEvent, args=("4"))
        keyboard.add_hotkey('f', self.processPersonelLeavingEvent,  args=("4"))
        keyboard.wait('esc')
    
    