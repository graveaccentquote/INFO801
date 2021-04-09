# -*- coding: utf-8 -*-
from rx import Observable
from rx import operators as ops
from rx import create
from rx.subject import Subject
from multiprocessing import Process

from fireAlarm import FireAlarm

if __name__ == '__main__':
    alarm = Subject()
    ui = FireAlarm(alarm)
    alarm.subscribe(
        lambda x: print("Alarm {0}".format(x))
    )
    ui.keyboardEvent()