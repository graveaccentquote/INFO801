# -*- coding: utf-8 -*-
from rx import Observable
from rx import operators as ops
from rx import create
from rx.subject import Subject
from rx.subject import AsyncSubject
import keyboard  # using module keyboard
from multiprocessing import Process

class FireAlarm(object):

    def __init__(self, subject):
        self.subject_keyboard = Subject()
        self.alarm = subject
        self.subject_keyboard.subscribe(
            lambda x: print("Alarm ready {0}".format(x))
        )
        self.subject_keyboard.subscribe(
            lambda y: self.alarm.on_next("A")
        )
        
    def keyboardEvent(self):
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    self.subject_keyboard.on_next("A")
                    break  # finishing the loop
            except:
                break  # if user pressed a key other than the given key the loop will break