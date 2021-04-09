# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:42:33 2021

@author: C Ost
"""


from multiprocessing import Process, Manager

def myf(myd):
    myd[1] = "HELLO WORLD!"

def proc(d):
    myf(d)


if __name__ == '__main__':
    m=Manager()
    locdict=m.dict()
    locdict[2] = "HI BUDDY!"
    
    p = Process(target=proc, args=(locdict,))
    
    p.start()
    p.join()
    print(locdict)
    