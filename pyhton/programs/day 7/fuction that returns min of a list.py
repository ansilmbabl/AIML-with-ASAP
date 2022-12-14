#WAP to sort a list using functions

#define a fuction that returns min of a list


def minl(l):
    
##    l=list(map(int,input("enter the numbers by comma: ").split()))
    s=l[0]
    for i in range(len(l)):
        if l[i]<s:
            s=l[i]
    return s
    
##print(minl([45,12,3,78,65,846,25])   

def list_sort(l):
    sortedlist=[]
    for i in range(len(l)):
        minim=minl(l)
        sortedlist.append(minim)
        l.remove(minim)
    return sortedlist

l = [13,5,135,6,5,84,3,845,84,3,64,83,9,56]
print(list_sort(l))
