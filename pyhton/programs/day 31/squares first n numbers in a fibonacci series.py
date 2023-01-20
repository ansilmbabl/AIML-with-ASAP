def fibsqr(n):
    a=0
    b=1
    for i in range(n):
        yield a*a
        a,b = b,a+b
        
l= [i for i in fibsqr(10)]
print(l)  
print(sum(l))
