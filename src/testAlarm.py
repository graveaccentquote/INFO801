from fireAlarm import fireAlarm
from rx import Observable
from rx import operators as ops
from rx import create
import keyboard  # using module keyboard
from multiprocessing import Process
from pymitter import EventEmitter

ee = EventEmitter()

@ee.on("myevent")
def handle_event( sender ):
    print (sender)

def alarm_observable(observer, scheduler):
   observer.on_next("Alarm")
   observer.on_completed()

if __name__ == '__main__':
    fAlarm = Process(target=fireAlarm, args=(ee,))
    fAlarm.start()