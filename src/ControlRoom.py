# -*- coding: utf-8 -*-
import memcache

def initPersonelList():
    personelList = {
        '1' : {'name' : 'Jean', 'id' : '1'},
        '2' : {'name' : 'Pierre', 'id' : '2'},
        '3' : {'name' : 'Marc', 'id' : '3'},
        '4' : {'name' : 'Paul', 'id' : '4'}
    }   
    return personelList
    

class ControlRoom(object):
    
    def __init__(self, debug=False):
        self.buildingMap = {}
        self.debug = debug
        self.personelList = {}
        
        
    def addBuilding(self,
                    buildingName="default_name",
                    address='127.0.0.1:11211'):
        sharedMemory = memcache.Client([address], debug=self.debug)
        self.buildingMap[buildingName] = {
            'name' : buildingName, 
            'address' : address, 
            'memory' : sharedMemory,
            'personel' : []
            }
     
    # takes a building name as parameter, polls the list of personel currently
    # in that building by reading the shared_memory (tuple space) attached to
    # said building.
    def pollCurrentlyInPersonel(self, buildingName):
        sharedMemory = self.buildingMap[buildingName]['memory']
        
        for personelId in self.buildingMap[buildingName]['personel']:
            read = sharedMemory.get(personelId)
            print(read)
    
    def addAccess(self, personelId, buildingName):
        sharedMemory = self.buildingMap[buildingName]['memory']
        
        personel = self.personelList[personelId]
        
        sharedMemory.set(personel['id'], {
            'id': personel['id'],
            'name' : personel['name'],
            'status' : 'AUTHORIZED'
            })
        
        self.buildingMap[buildingName]['personel'].append(personel['id'])
    
    def removeAccess(self, personelId, buildingName):
        building = self.buildingMap[buildingName]
        
        sharedMemory = building['memory']
        
        personel = self.personelList[personelId]
        
        sharedMemory.set(personel['id'], None)
        
        building['personel'].remove(personel['id'])
        
        
if __name__ == '__main__':
    controlRoom = ControlRoom(debug=True)
    controlRoom.personelList = initPersonelList()
    controlRoom.addBuilding("8C - Chartreuse")
    controlRoom.addAccess('1', "8C - Chartreuse")
    controlRoom.addAccess('2', "8C - Chartreuse")
    controlRoom.pollCurrentlyInPersonel("8C - Chartreuse")
    
    controlRoom.removeAccess('1', "8C - Chartreuse")
    controlRoom.pollCurrentlyInPersonel("8C - Chartreuse")