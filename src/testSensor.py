# -*- coding: utf-8 -*-
from rx import Observable
from rx import operators as ops
from rx import create
from rx.subject import Subject
from multiprocessing import Process, Queue

from sensor import Sensor

if __name__ == '__main__':
    #Subject
    opening = Subject()
    indicator = Subject()
    alarm = Subject()

    #Queue
    queue = Queue()

    #Object
    ui = Sensor(opening, indicator, alarm, queue)

    #Subscribes
    alarm.subscribe(
        lambda x: print("Alarm {0}".format(x))
    )

    indicator.subscribe(
        lambda x: print("Indicator {0}".format(x))
    )
    indicator.subscribe(
        lambda x: print(queue.put("something"))
    )
    indicator.subscribe(
        lambda x: print(queue.put("something"))
    )

    #Start
    opening.on_next("")
