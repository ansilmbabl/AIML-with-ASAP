

"""
iterative
"""


def num1(n):
    k=0
    while (2**k) <= n:
        k+=1
    return (k-1)


"""
recursive
"""

def num2(n,k):
    global x
    if 2**k <= n:
        x+=1
        return num2(n,k+1)
    else:
        return (x-1)


x=0
n=int(input("enter the limit of n: "))
print("iterative",num1(n))
print("recursive",num2(n,0))


