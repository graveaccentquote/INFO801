# -*- coding: utf-8 -*-
from rx import Observable
from rx import operators as ops
from rx import create
from rx.subject import Subject
from multiprocessing import Process, Queue
import time

from sensor import Sensor

def loveIsAnOpenDoor():
    counter = 0
    timeout = time.time() + 5
    while(time.time() < timeout):
        if(not(queue.empty())):
            counter += 1
            queue.get()
            if(counter >= 2):
                alarm.on_next("")
                return 0


if __name__ == '__main__':
    #Subject
    opening = Subject()
    indicator = Subject()
    alarm = Subject()

    #Queue
    queue = Queue()

    #Object
    ui = Sensor(opening, indicator, queue)

    #Subscribes
    alarm.subscribe(
        lambda x: print("Alarm {0}".format(x))
    )

    indicator.subscribe(
        lambda x: print("Indicator {0}".format(x))
    )

    #Start
    opening.on_next("")
    loveIsAnOpenDoor()