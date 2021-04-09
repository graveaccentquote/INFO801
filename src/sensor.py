# -*- coding: utf-8 -*-
from rx import operators as ops
from rx import create
from rx.subject import Subject
from multiprocessing import Process
import time

class Sensor(object):
    
    def __init__(self, subject_opening, subject_indicator, subject_alarm, queue):
        self.opening = subject_opening
        self.indicator = subject_indicator
        self.alarm = subject_alarm
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
        cpt = 0
        timeout = time.time() + 5
        while(time.time() < timeout):
            if(not(self.queue.empty())):
                cpt += 1
                self.queue.get()
            if(cpt == 2):
                self.alarm.on_next("")
                break


