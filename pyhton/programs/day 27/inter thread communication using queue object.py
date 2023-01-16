## inter thread communication
## using queue object

from threading import*
from queue import Queue
from time import sleep

n = int(input("enter the number of students: "))
q=Queue(n+1)

def producer(q):
    print("producer : running")
    for i in range(n):
        mark = int(input("etner the marks: "))
        q.put(mark)
        sleep(0.5)
    q.put(None)

def consumer(q):
    print("consumer: running")
    while True:
        mark = q.get()
        if mark == None:
            break
        else:
            print("Got the item", mark)
    print("consumer: done")


t1 = Thread(target = producer,args=(q,))
t2 = Thread(target = consumer,args=(q,))

t1.start()
t2.start()
