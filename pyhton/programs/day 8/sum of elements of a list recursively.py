#sum of elements of a list recursively



def total(l):
    if len(l)==0:        
        return 0
    else:
        return l[0]+total(l[1:])

l=list(map(int,input("enter a lsit by comma : ").split(",")))
print("sum is = ",total(l))



