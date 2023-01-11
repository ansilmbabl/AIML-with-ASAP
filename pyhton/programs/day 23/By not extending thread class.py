#multitasking in python (threading)

##By not extending thread class
from threading import*

class myThread():
    def myFun(self):
        for i in range(5):
            print("child thread")

m=myThread()
t1=Thread(target = m.myFun) #creating thread object
t1.start() 
# t1.join() #exceute like ther is no multitasking
for i in range(5):
    print("parent thread")

