#WAP to sort list of elements recersively

##def sort(l):
##    n=[]
##    if len(l)== 0:
##        return n
##    else:
##        n.append(min(l))
##        return sort(l.pop(min(l)))
##        return n

l=list(map(int,input("enter a lsit by comma : ").split(",")))
print(sort(l))


def min(l):
    small=l[0]
    for i in l:
        if i<small:
            small=i
    return small

def sort(l):
    if len(l)==0:
        return l
    else:
        m=min(l)
        l.remove(m)
        return [m]+sort(l)
