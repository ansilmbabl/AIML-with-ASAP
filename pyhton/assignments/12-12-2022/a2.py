

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
    

def n_mat(l):
    for i in l[1:len(l)-1]:
        for k in range(1,len(i)-1):
            i[k]=0
    return l
    
def display(l):
    for i in l:
        for j in i:
            print(j,end=" ")
        print()

print("your matrix is ")
l= mat(m,n)
display(l)
        

print("new matrix is ")
display(n_mat(l))
