#WAP to find aveerage of a set of nubers using functions

def total(a):
    t=0
    for i in a:
        t+=i
        return t
l=[2,4,6,8,9,10,12]
print(total(l)/len(l))
