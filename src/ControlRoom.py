# -*- coding: utf-8 -*-

import memcache


def initPersonelList():
    personelList = []
    personelList.append({
        'name' : 'Name1',
        'id' : 1})
    personelList.append({
        'name' : 'Name2',
        'id' : 2})
    personelList.append({
        'name' : 'Name3',
        'id' : 3})
    personelList.append({
        'name' : 'Name4',
        'id' : 4})
    

class ControlRoom(object):
    
    def __init__(self, debug=False):
        self.buildingMap = {}
        self.debug = debug
        self.personelList = []
        
        
    def addBuilding(self, buildingName="default_name", address='127.0.0.1:11211'):
        sharedMemory = memcache.Client([address], debug=self.debug)
        self.buildingMap[buildingName] = {
            'name' : buildingName, 
            'address' : address, 
            'memory' : sharedMemory
            }
     
    # takes a building name as parameter, polls the list of personel currently
    # in that building by reading the shared_memory (tuple space) attached to
    # said building.
    def pollCurrentlyInPersonel(self, buildingName):
        sharedMemory = self.buildingMap[buildingName]['memory']
        #for element in sharedMemory:
        #    print(element)
    
    def addAccess(self, personelId, buildingName):
        sharedMemory = self.buildingMap[buildingName]['memory']
        
        personel = self.personelList[personelId]
        
        sharedMemory.set(personel['id'], {
            'id': personel['id'],
            'name' : personel['name'],
            'status' : 'AUTHORIZED'
            })
    
    def removeAccess(self, personelId, buildingName):
        #del self.currentPersonel[personelId]
        print()
        
        
if __name__ == '__main__':
    controlRoom = ControlRoom(debug=True)
    controlRoom.personelList = initPersonelList()
    controlRoom.addBuilding("8C - Chartreuse")
    
    
    #controlRoom.addAccess(1, "8C - Chartreuse")
    controlRoom.pollCurrentlyInPersonel("8C - Chartreuse")