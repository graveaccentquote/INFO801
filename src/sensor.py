# -*- coding: utf-8 -*-
import keyboard  # using module keyboard
#import time
from multiprocessing import Queue

def writeInQueue(queue, arg):
    queue.put(arg)
                
def sensor(queue):
    keyboard.add_hotkey('s', writeInQueue, args=(queue, 'triggered'))
    keyboard.wait('esc')
    
    while (not queue.empty()):
        print(queue.get())
    #time.sleep(1)
    


if __name__ == '__main__':
    queue = Queue()
    sensor(queue)