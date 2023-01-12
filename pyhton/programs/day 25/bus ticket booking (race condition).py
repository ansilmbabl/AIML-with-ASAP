#bus ticket booking (race condition)

from threading import *
import time

class bus:
    def __init__(self,name,available): # availabale seats
        self.availabale = available
        self.name = name

    def reserve(self,needed): #needed seats
        print("Availabale seats are : ",self.availabale)
        if self.availabale >= needed:
            print(f"{needed} seats are allocated to ",current_thread().name) # current_thread().name = thread name
            self.availabale -= needed
        else:
            print("sorry, seats are not available")
        time.sleep(0.5)

b1 = bus("ABC travels",5)

t1 = Thread(target = b1.reserve,args=(2,),name="Rakesh") #name thread = Rakesh
t2 = Thread(target = b1.reserve,args=(3,),name="Akshaya")
t3 = Thread(target = b1.reserve,args=(1,),name="Praveen")

t1.start()
t2.start()
t3.start()


##in this case seats are alllocated to all using at the same time since race condition is not given
## hence we need to lock the shared region where multiple threads are accessing ()
## this is called thread synchronisation

