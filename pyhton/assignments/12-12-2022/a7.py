

l=[12,56,3,64,3,64,44,31,45,62,87,21,9,78,12,62,78,65,12,6,5,2,100,45,95]

def avg(l):
    s = 0
    for i in l:
        s+=i
    avg = s/len(l)
    return avg

def med(l):
    l.sort()
    m= l[len(l)//2]
    return m

def mod(l):
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    n=list(d.values())
    return max(n)
    

def small(l):
    s=0
    for i in l[:len(l)-2]:
        for j in l[i+1:]:
            if i<j:
                s=i
            else:
                s=j
        break
    return s
                

print("class average = ",avg(l))
print("median mark = ",med(l))
print("mod = ",mod(l))
print("smallest mark = ",small(l))
