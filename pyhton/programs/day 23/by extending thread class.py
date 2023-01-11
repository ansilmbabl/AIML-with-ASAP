#multitasking in python (threading)


##By extending thread class
from threading import*

class myThread(Thread):
    def run(self):
        for i in range(5):
            print("child thread")

m=myThread()
m.start()
# m.join() #exceute like ther is no multitasking
for i in range(5):
    print("parent thread")
