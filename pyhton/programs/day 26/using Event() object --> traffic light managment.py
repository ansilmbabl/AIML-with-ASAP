## inter thread communication
## using Event() object
## traffic light managment

from threading import *
import time

e=Event()

def color():
    while (True):
        print("* GREEN * ")
        e.set()
        time.sleep(5)
        print("*** RED *** STOP THERE ***")
        e.clear()
        time.sleep(5)


def msg():
    e.wait()
    while e.is_set():
        print(" You can go now....")
        time.sleep(1)
        e.wait()

t1 = Thread(target = color)
t2 = Thread(target = msg)

t1.start()
t2.start()
