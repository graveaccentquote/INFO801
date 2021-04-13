# -*- coding: utf-8 -*-

import memcache
from multiprocessing import Process, Queue

from sensor import sensor

import time

class Door(object):
    
    def __init__(self, door_in, timeout=5, port=11211, debug=0):
        self.debug = debug
        self.timeout = timeout
        
        self.door_in = door_in
                
        address = '127.0.0.1:'+str(port)
        self.sharedMemory = memcache.Client([address], debug=debug)

        self.debug = debug == 1
        
    
    #check an id to see if it's currently allowed to get in or out
    def checkId(self, personelId):
        #read the tuple
        t = self.sharedMemory.get(personelId)
        
        result = t["status"] == "AUTHORIZED" or t["status"] == "CURRENTLY INSIDE"
    
        return result
    
    
    def doorProtocol(self, personelId):
        count = 0
        while((time.time() - t ) < self.timeout):
            if (not door_in.empty()):
                print(door_in.get(block=False))
                count = count + 1
                if (count > 1):
                    print("alarm")
                else:
                    #todo : change person to currently in/out
                    print("in")
            

if __name__ == '__main__':
    door_in = Queue()
    d = Door(door_in)

    sensor_process = Process(target=sensor, args=(door_in,))
        
    sensor_process.start()
    t = time.time()
    
    while((time.time() - t ) < 2):
        if (not door_in.empty()):
            print(door_in.get())