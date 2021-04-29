# -*- coding: utf-8 -*-
import keyboard  # using module keyboard
#import time
from multiprocessing import Queue


class doorSensor(object):
    
    def __init__(self, queueIn):
        self.queueIn = queueIn

def writeInQueue(queue, arg):
    print("SENSOR HAS BEEN TRIGGERED")
    queue.put(arg)
                
def sensor(queue):
    keyboard.add_hotkey('s', writeInQueue, args=(queue, 'triggered'))
    keyboard.wait('esc')
    
if __name__ == '__main__':
    queue = Queue()
    sensor(queue)
    
    while (not queue.empty()):
        print(queue.get())
    #time.sleep(1)
    
    
# t = threading.Thread(target=sys.stdin.read(1) args=(1,))
# t.start()
# time.sleep(5)
# t.join()