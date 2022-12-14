def seq(l):
    n=[]
    for i in l:
        if i not in n:
            n.append(i)
    return n

def display(l):
    for i in l:
        print(i,end=",")



l=list(map(int,input("enter the numbers seperated by comma: ").split(",")))

display(seq(l))
