

def avg(l):
    a=0
    for i in l:
        a+=i
    av = a/len(l)
    return av

def seq(l):
    n=[]
    for i in l:
        if i > avg(l):
            n.append(i)
    return n

def display(l):
    l.sort()
    for i in l:
        print(i,end=" ")





l=list(map(int,input("enter the numbers seperated by space: ").split(" ")))

display(seq(l))
