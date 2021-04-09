# -*- coding: utf-8 -*-
from rx import operators as ops
from rx import create
from rx.subject import Subject
from multiprocessing import Process
import keyboard  # using module keyboard
import time

class Sensor(object):
    
    def __init__(self, subject_opening, subject_indicator, queue):
        self.opening = subject_opening
        self.indicator = subject_indicator
        self.queue = queue
        self.opening.subscribe(
            lambda x: print("Sensor is listening".format(x))
        )
        self.opening.subscribe(
            lambda x: self.indicator.on_next("")
        )
        self.opening.subscribe(
            lambda x: self.activate_sensor()
        )

    def activate_sensor(self):
        timeout = time.time() + 5
        while(time.time() < timeout):
            if keyboard.is_pressed('s'):  # if key 's' is pressed 
                print("someone's entering")
                self.queue.put("someone's entering")
                time.sleep(0.5)



