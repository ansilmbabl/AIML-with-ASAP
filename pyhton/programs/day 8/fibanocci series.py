#WAP to print n numbers in the fibanocci series

##def fib(n):
##    
##    l=[0,1]
##    x=l[-1]+l[-2]
##    l.append(x)
##    if len(l)<= n:
##        return fib(n)
##
##n=int(input("enter numbers in list: "))
##print(fib(n))

def fibrec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return(fibrec(n-1)+fibrec(n-2))

n=int(input("enter numbers in list: "))
for i in range(n):
    print(fibrec(i),end=" ")
## non recursive (iteration)

##def fib(n):
##    f1=0
##    f2=1
##    print(f1,end="")
##    for i in range(1,n):
##        print(f2,end="")
##        nxt=f1+f2
##        f1=f2
##        f2=nxt
##
##n=int(input("enter numbers in list: "))
##fib(n)
