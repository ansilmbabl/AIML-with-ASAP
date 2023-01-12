##locking thread 3 (Semaphore)

from threading import*
import time

obj = Semaphore(2) #craating an object in class Semaphore
#obj = Lock() #if Lock is used threads will be executed one by one


def display():
    obj.acquire()
    for i in range(1):
        print("hello..",current_thread().name)
    obj.release()
    time.sleep(0.5)
    

t1= Thread(target = display)
t2= Thread(target = display)
t3= Thread(target = display)
t4= Thread(target = display)
t5= Thread(target = display)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
