# -*- coding: utf-8 -*-
import memcache  

class ControlRoom(object):
    
    def __init__(self,
                 memCacheAddress='127.0.0.1:11211',
                 debug=0
                 ):
        
        self.debug=debug
        self.sharedMemory = memcache.Client([memCacheAddress], debug=debug)
        
        self.sharedMemory.set("idList", [])
            
    def addPersonel(self, personelId, name):       
        personel = {
            'name': name,
            'id' : personelId,
            'auth' : [],
            'location' : "outside"
            }
        
        self.sharedMemory.set(personelId, personel)    
        
        idList = self.sharedMemory.get("idList")
        idList.append(personelId)
        self.sharedMemory.set("idList", idList)
        
        
                
    def authorizePersonel(self, personelId, buildingName):
        result = self.sharedMemory.get(personelId)
        
        if result is None:
            print("Error, personel id not found")
            return
    
        result['auth'].append(buildingName)
        self.sharedMemory.set(personelId, result)
        
    def deauthorizePersonel(self, personelId, buildingName):
        result = self.sharedMemory.get(personelId)
        
        if result is None:
            print("Error, personel id not found")
            return
        
        if buildingName not in result['auth']:
            print("Error, building \"" 
                  + buildingName 
                  + "\" not found in authorizations of user "
                  + result['name'])
            return
            
        result['auth'].remove(buildingName)
        
        self.sharedMemory.set(personelId, result)
             
    # takes a building name as parameter, polls the list of personel currently
    # allowed in that building by reading the shared_memory (tuple space)
    def pollPersonel(self, buildingName):
        acc = []
        
        idList = self.sharedMemory.get("idList")
        
        for pId in idList:
            result = self.sharedMemory.get(pId)
            
            if buildingName in result['auth']:
                acc.append(result['name'])
                
        return acc
    
    # polls the list of personel and their authorizations
    def listPersonel(self):
        acc = []
        
        idList = self.sharedMemory.get("idList")
        
        for pId in idList:
            result = self.sharedMemory.get(pId)
            acc.append(result)
                
        return acc
    
    #init for demo
    def initDemo(self):
        self.addPersonel("1", "Jean")
        self.authorizePersonel("1", "8C - Chartreuse")
        self.authorizePersonel("1", "3 - Pôle Montagne")
        self.addPersonel("2", "Pierre")
        self.authorizePersonel("2", "8C - Chartreuse")
        self.addPersonel("3", "Marc")
        self.addPersonel("4", "Paul")
            
        
if __name__ == '__main__':
    controlRoom = ControlRoom(debug=1)
    controlRoom.initDemo()
    
    #test adding/removing auths
    # print(controlRoom.sharedMemory.get("idList"))
    # print(controlRoom.listPersonel())
    # print(controlRoom.pollPersonel("8C - Chartreuse"))
    # controlRoom.deauthorizePersonel("2", "8C - Chartreuse")
    # print(controlRoom.pollPersonel("8C - Chartreuse"))