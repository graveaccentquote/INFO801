# -*- coding: utf-8 -*-
import keyboard  # using module keyboard

    
class FireAlarm(object):
    
    def __init__(self, key, ee):
        self.key = key
        self.ee = ee
        
    def triggerFireAlarm(self):
        self.ee.emit("fireAlarmEvent",)
        
    def listenKB(self):
        keyboard.add_hotkey(self.key, self.triggerFireAlarm, args=())
        keyboard.wait('esc')
        print("stoping listening to keyboard")
        