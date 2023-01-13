## inter thread communication
## using Event() object

from threading import*
import time

e=Event() #creating an object 

def task():
    for i in range(5):
        print("The game is running")
        time.sleep(1)
    e.set() #give signal to next thread by changing flag to True

def end():
    e.wait()
    #e.wait(timeout = 3) #wait for only 3 seconds
    if e.is_set():
        print("Game over...!")

t1 = Thread(target = task)
t2 = Thread(target = end)

t1.start()
t2.start()
