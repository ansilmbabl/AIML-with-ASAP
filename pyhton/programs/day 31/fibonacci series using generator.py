def fib(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b
        
for x in fib(10):
    print(x)
