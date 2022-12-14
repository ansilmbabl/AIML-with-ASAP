# find factorial of a number recersively

def f(l):
    if l==1 or l== 0:
        return 1
    if l!=1:
        return (l* f(l-1))
    

l=int(input("enter number : "))
print("factorial is : ",f(l))
