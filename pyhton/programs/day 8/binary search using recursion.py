##binary search using recursion


def bins(l,x):
    l.sort()
    if len(l)== 0:
        print(x," not found")
    elif x == l[len(l)//2]:
        print(x," found")
    elif x>l[len(l)//2]:
        return bins(l[(len(l)//2)+1:],x)
##    elif x<l[len(l)//2]:
    else:
        return bins(l[:len(l)//2],x)
##    else:
##        print(x," not found")

l=list(map(int,input("enter a lsit by comma : ").split(",")))
x=int(input("number to be found : "))

bins(l,x)
