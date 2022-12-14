

def mul(x,y):
    s=0
    if y>0:
        s = x + (mul(x,y-1))
    return s

x = int(input("enter number 1: "))
y = int(input("enter number 2: "))
print("result",mul(x,y))
