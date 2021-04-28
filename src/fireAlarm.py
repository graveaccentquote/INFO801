# -*- coding: utf-8 -*-
from rx import Observable
from rx import operators as ops
from rx import create
import keyboard  # using module keyboard
from multiprocessing import Process

def triggerFireAlarm(subject):
    subject.subscribe(
        on_next = lambda i: print("Got - {0}".format(i)),
        on_error = lambda e: print("Error : {0}".format(e)),
        on_completed = lambda: print("Job Done!"),
    )

def fireAlarm(subject):
    keyboard.add_hotkey('q', triggerFireAlarm, args=(subject, ))
    keyboard.wait('esc')