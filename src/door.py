# -*- coding: utf-8 -*-

import memcache
from multiprocessing import Process, Queue

from sensor import sensor

import time


## class representing a door,a door is part of a building, and is linked to 1 
# sensor and contains 2 badge readers

class Door(object):
    
    def __init__(self, sensorQueue, timeout=5, port=11211, debug=0):
        self.debug = debug
        self.timeout = timeout
        
        self.sensorQueue = sensorQueue
                
        address = '127.0.0.1:'+str(port)
        self.sharedMemory = memcache.Client([address], debug=debug)

        self.debug = debug == 1
        
    def switchPersonelStateToOut(self):
        print("test")
        
    
    #check an id to see if a person is currently allowed to get in
    def checkIdForExit(self, personelId):
        #read the tuple
        t = self.sharedMemory.get(personelId)
        status = t["status"]
        
        if status == "CURRENTLY INSIDE":
            print("Opening door")
            return True           
        elif status == "AUTHORIZED":
            print("Error, personel is already outside")
            return False
        else :
            print("Error, personel not found")
            return False
    
    #check an id to see if a person is currently allowed to get out
    def checkIdFOrEntering(self, personelId):
        #read the tuple
        t = self.sharedMemory.get(personelId)
        
        status = t["status"]
        
        if status == "AUTHORIZED":
            print("Opening door")
            return True           
        elif status == "CURRENTLY INSIDE":
            print("Error, personel is already inside")
            return False
        else :
            print("Error, personel not found")
            return False
    
    def exitProtocol(self, personelId):
        #create new queue, give it to the sensor via mobility
        q = Queue()        
        self.sensorQueue.put(q)
        
        #wait for timeout seconds while counting the messages received on q
        count = 0
        while((time.time() - t ) < self.timeout):
            if (not sensorQueue.empty()):
                sensorQueue.get(block=False)
                count += 1
                
                #if first time, everything is fine, switch the state in mem
                if count == 1:
                    self.switchPersonelStateToOut()
                #if more than 1 person detected, trigger alarm
                else:
                    self.triggerAlarm()
                    break
                
    def enteringProtocol(self, personelId):
        #create new queue, give it to the sensor via mobility
        q = Queue()        
        self.sensorQueue.put(q)
        
        #wait for timeout seconds while counting the messages received on q
        count = 0
        while((time.time() - t ) < self.timeout):
            if (not sensorQueue.empty()):
                sensorQueue.get(block=False)
                count += 1
                
                #if first time, everything is fine, switch the state in mem
                if count == 1:
                    self.switchPersonelStateToIn(personelId)
                #if more than 1 person detected, trigger alarm
                else:
                    self.triggerAlarm()
                    break
            

if __name__ == '__main__':
    sensorQueue = Queue()
    d = Door(sensorQueue)

    sensor_process = Process(target=sensor, args=(sensorQueue,))
        
    sensor_process.start()
    t = time.time()
    
    while((time.time() - t ) < 2):
        if (not sensorQueue.empty()):
            print(sensorQueue.get())