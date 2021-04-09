from fireAlarm import FireAlarm
from rx import Observable
from rx import operators as ops
from rx import create
from rx.subject import Subject
from rx.subject import AsyncSubject
import keyboard  # using module keyboard
from multiprocessing import Process


if __name__ == '__main__':
    alarm = Subject()
    ui = FireAlarm(alarm)
    alarm.subscribe(
        lambda x: print("Alarm {0}".format(x))
    )
    ui.keyboardEvent()