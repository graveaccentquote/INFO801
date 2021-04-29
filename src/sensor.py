# -*- coding: utf-8 -*-
import keyboard
from multiprocessing import Queue


def writeInQueue(queue, arg):
    print("SENSOR HAS BEEN TRIGGERED")
    queue.put(arg)
                
def sensor(key, queue):
    keyboard.add_hotkey(key, writeInQueue, args=(queue, 'triggered'))
    keyboard.wait('esc')
    
if __name__ == '__main__':
    queue = Queue()
    sensor(queue)
    
    while (not queue.empty()):
        print(queue.get())
    #time.sleep(1)