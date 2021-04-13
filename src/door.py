# -*- coding: utf-8 -*-

import memcache

class DoorController(object):
    
    def __init__(self, buildingName="default_name", port=11211, debug=0):
        self.debug = debug
        self.parentBuildingName = buildingName
                
        address = '127.0.0.1:'+str(port)
        self.sharedMemory = memcache.Client([address], debug=debug)

        self.debug = debug == 1
        
    
    #check an id to see if it's currently allowed to get in or out
    def checkId(self, personelId):
        #read the tuple
        t = self.sharedMemory.get(personelId)
        
        result = t["status"] == "AUTHORIZED" or t["status"] == "CURRENTLY INSIDE"
    
        return result
    
    