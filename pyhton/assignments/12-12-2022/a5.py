

"""
iterative
"""


def m1(n):
    s = 0
    for i in range(0,n):
        x = 2**i
        s += x
    return s


"""
recursive
"""

def m2(n):
    s = 0
    if n-1 >= 0:
        x = 2**(n-1)+ m2(n-1)
        s += x
        
    return s

n=int(input("enter the number of iteration: "))
print("iterative",m1(n))
print("recursive",m2(n))
