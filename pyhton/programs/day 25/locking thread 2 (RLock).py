##locking thread 2 (RLock)

from threading import *
import time

class bus:
    l=RLock() # now we can use aquire many times
    def __init__(self,name,available): # availabale seats
        self.availabale = available
        self.name = name

    def reserve(self,needed): #needed seats
        self.l.acquire() #locking
        self.l.acquire()
        print("\n\nAvailabale seats are : ",self.availabale)
        print(self.l) # detail of thread after locking
        if self.availabale >= needed:
            print(f"{needed} seats are allocated to ",current_thread().name) # current_thread().name = thread name
            self.availabale -= needed
        else:
            print("sorry, seats are not available to ",current_thread().name)
        time.sleep(0.5)
        self.l.release() #releasing lock
        self.l.release()
        print(self.l) # detail of thread after unlocking

b1 = bus("ABC travels",3)

t1 = Thread(target = b1.reserve,args=(2,),name="Rakesh") #name thread = Rakesh
t2 = Thread(target = b1.reserve,args=(3,),name="Akshaya")
t3 = Thread(target = b1.reserve,args=(1,),name="Praveen")

t1.start()
t2.start()
t3.start()

