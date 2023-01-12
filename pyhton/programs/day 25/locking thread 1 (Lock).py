##locking thread 1

from threading import *
import time

class bus:
    l=Lock() #Lock is a class inside threading module
    def __init__(self,name,available): # availabale seats
        self.availabale = available
        self.name = name

    def reserve(self,needed): #needed seats
        self.l.acquire() #locking
        print("Availabale seats are : ",self.availabale)
        if self.availabale >= needed:
            print(f"{needed} seats are allocated to ",current_thread().name) # current_thread().name = thread name
            self.availabale -= needed
        else:
            print("sorry, seats are not available to ",current_thread().name)
        time.sleep(0.5)
        self.l.release() #releasing lock

b1 = bus("ABC travels",3)

t1 = Thread(target = b1.reserve,args=(2,),name="Rakesh") #name thread = Rakesh
t2 = Thread(target = b1.reserve,args=(3,),name="Akshaya")
t3 = Thread(target = b1.reserve,args=(1,),name="Praveen")

t1.start()
t2.start()
t3.start()

