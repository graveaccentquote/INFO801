from fireAlarm import fireAlarm
from rx import Observable
from rx import operators as ops
from rx import create
import keyboard  # using module keyboard
from multiprocessing import Process
from threading import Thread


def alarm_observable(observer, scheduler):
   observer.on_next("Alarm")
   observer.on_completed()

if __name__ == '__main__':
    alarm = create(alarm_observable)
    fAlarm = Thread(target=fireAlarm, args=(alarm,))
    fAlarm.start()