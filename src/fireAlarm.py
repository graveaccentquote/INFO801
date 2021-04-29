# -*- coding: utf-8 -*-
from rx import Observable
from rx import operators as ops
from rx import create
import keyboard  # using module keyboard
from multiprocessing import Process
from pymitter import EventEmitter

def triggerFireAlarm(ee,):
    ee.emit("myevent", "foo")

def fireAlarm(ee):
    keyboard.add_hotkey('q', triggerFireAlarm, args=(ee,))
    keyboard.wait('esc')