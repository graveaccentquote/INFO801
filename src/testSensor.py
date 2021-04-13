# -*- coding: utf-8 -*-
from rx import Observable
from rx import operators as ops
from rx import create
from rx.subject import Subject
from multiprocessing import Process, Queue
import time
import threading


from sensor import Sensor

def loveIsAnOpenDoor():
    counter = 0
    timeout = time.time() + 20
    while(time.time() <= timeout):
        if(not(queue.empty())):
            counter += 1
            queue.get()
            if(counter >= 2):
                alarm.on_next("")
                break


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
    #x = threading.Thread(target=loveIsAnOpenDoor, args=())
    #x.start()
    
    x = Process(target=loveIsAnOpenDoor, args=(alarm, queue,))
    x.start()
    
    opening.on_next("")