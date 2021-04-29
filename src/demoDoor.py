# -*- coding: utf-8 -*-
from sensor import sensor
from door import Door
from multiprocess import Process, Queue

if __name__ == '__main__':
    sensorQueue = Queue()
    d = Door("Nord", "8C - Chartreuse", sensorQueue)

    sensor_process = Process(target=sensor, args=('t', sensorQueue,))
    sensor_process.start()
    
    d.listenKeyboard()