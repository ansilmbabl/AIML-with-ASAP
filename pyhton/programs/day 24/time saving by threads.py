#adv of threading

##import time #for getting time 
##
##class Calc:
##    def sqr(self,n): #list n
##        print("squares")
##        for i in n:
##            time.sleep(1) #for seeig execution (time delay)
##            print(i*i)
##
##    def cube(self,n):
##        print("cubes")
##        for i in n:
##            time.sleep(1) #for seeig execution (time delay)
##            print(i*i*i)
##
##c=Calc()
##n=[1,2,3,4,5]
##start_time = time.time() #time function returns current time
##c.sqr(n)
##print()
##c.cube(n)
##end_time = time.time()
##
##print("time taken for calculation")
##print(end_time - start_time)


####by using thread
from threading import*
import time #for getting time 

class Calc:
    def sqr(self,n): #list n
        print("squares\t")
        for i in n:
            time.sleep(1) #for seeig execution (time delay)
            print(f"{i*i}\t")

    def cube(self,n):
        print("cubes\t")
        for i in n:
            time.sleep(1) #for seeig execution (time delay)
            print(f"{i*i*i}\t")

c=Calc()
n=[1,2,3,4,5]

t1 = Thread(target = c.sqr,args=[n]) #for morethan one argument we pass a tuple
t2 = Thread(target = c.cube,args=[n])

start_time = time.time() #time function returns current time

t1.start()
t2.start()
t1.join()
t2.join()

end_time = time.time()

print("time taken for calculation")
print(end_time - start_time) ## it reduced time to almost half of its original
