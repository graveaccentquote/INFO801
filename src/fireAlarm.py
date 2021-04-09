# -*- coding: utf-8 -*-
from rx import operators as ops
from rx import create
from rx.subject import Subject
import keyboard  # using module keyboard
from multiprocessing import Process

class FireAlarm(object):

    def __init__(self, subject_fire_alarm):
        self.subject_keyboard = Subject()
        self.fire_alarm = subject_fire_alarm
        self.subject_keyboard.subscribe(
            lambda x: print("Alarm ready {0}".format(x))
        )
        self.subject_keyboard.subscribe(
            lambda x: self.fire_alarm.on_next("")
        )
        
    def keyboardEvent(self):
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    self.subject_keyboard.on_next("")
                    break  # finishing the loop
            except:
                break  # if user pressed a key other than the given key the loop will break