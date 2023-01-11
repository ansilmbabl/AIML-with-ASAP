#multitasking in python (threading)


##Normal thread creation (without using class)
from threading import*

def fun1():
    print("child thread")


child=Thread(target=fun1) #creating thread object
child.start() # both thread happens simultaneously
# child.join() #exceute like ther is no multitasking

print("parent thread")
