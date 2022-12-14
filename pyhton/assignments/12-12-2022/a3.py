m = int(input("number of rows: "))
n = int(input("number of columns: "))

def mat(m,n):
    l=[]
    for i in range(1,m+1):
        lm=[]
        for j in range(1,n+1):
            x=int(input(f"enter row {i} column {j} : "))
            lm.append(x)
        l.append(lm)
    return l
    

def r_mat(l):
    l=l[::-1]
    print(l)
    k=[]
    for i in l:
        k.append(i)
    return k
    
def display(l):
    for i in l:
        for j in i:
            print(j,end=" ")
        print()

print("your matrix is ")
l= mat(m,n)
display(l)
        

print("reversed matrix is ")
display(r_mat(l))
