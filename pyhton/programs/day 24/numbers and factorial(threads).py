#WAP using multi-thrading to assign two thread, one should print the number and another
#thread should print the facotorial of that number

from threading import*
import time

class num:
    def nu(self,n):
        time.sleep(1)
        print(f"number : {n}\t")
    def fac(self,n):
        time.sleep(1)
        f = 1
        for i in range(1,n+1):
            f = f*i
        print(f"factorial : {f}\t")

a=num()
n=int(input("enter number: "))

t1= Thread(target = a.nu,args=(n,))
t2= Thread(target = a.fac,args=(n,))

start = time.time()
t1.start()
t2.start()
time.sleep(1)
t1.join()
t2.join()
end = time.time()

print(end - start)



