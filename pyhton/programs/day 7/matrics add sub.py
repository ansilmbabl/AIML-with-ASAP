#WAP to get two matices from the user and perform addition and
##subtractoin,
##transpose on them
##sum of diagonal elements of square matrix


##def mat():
##    
##
##    l=[]
##    for i in range(r):
##        row=list(map(int,input(f"enter row {i}: ").split(",")))
##        l.append(row)
##        
##    for i in range(r):
##        for j in range(c):
##            print(l[i][j],end=" ")
##        print()
##
##def add():
##    if len(x) == len(y)
##
##c=int(input("columns: "))
##r=int(input("rows: "))
##
##mat()


def mat(r,c):
    l=[]
    for i in range(r):
        print("enter row ",i)
        r=[]
        for j in range (c):
            num=int(input())
            row.append(num)
        l.append(row)
    return l

def add(m,n):
    result=[]
    for i in range (len(m)):
        row=[]
        for j in range(len(m[0])):
            row.append(m[i][j] + n[i][j])
        result.append(row)
    return result

def sub(m,n):
    result=[]
    for i in range (len(m)):
        row=[]
        for j in range(len(m[0])):
            row.append(m[i][j] - n[i][j])
        result.append(row)
    return result

def tran(n):
    result=[]
    for i in range(len(n)):
        row=[]
        for j in range(len(n[0])):
            row.append(n[j][i])
        result.append(row)
    return result

def diagsum(n):
    if len(n)!=len(n[0]):
        return "not a square matrix"
    else:
        s=0
        for i in range(len(n)):
            for j in range(len(n[0])):
                if i == j:
                    s+= n[i][j]
        return s
                
def display(m):    
    for i in range (len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end=" ")
        print()



r1=int(input("rows of matrics 1:"))
c1=int(input("columns of matrics 1:"))
r2=int(input("rows of matrics 2:"))
c2=int(input("columns of matrics 2:"))

if r1!=r1 or c1!=c2:
    print("invalid selections")
else:
    print("first matrix")
    m= mat(r1,c1)
    print("second matrix")
    n= mat(r2,c2)
    display(m)
    print("\n\n")
    display(n)
    add(m,n)
    print("sum matrix is: ")
    display(add)
    print("difference matrix is: ")
    sub(m,n)
    display(sub)
    print("transpose of matrix :")
    display(tran(m))
    print(diagsum(m))





"""
# WAP to get two matrices from the user, perform addition and subtraction on them

# take_matrix()
# add_matrix()
# sub_matrix()


def take_matrix(r,c):
    l=[]
    for i in range(r):
        print("Enter row ",i)
        row=[]
        for j in range(c):
            num=int(input())
            row.append(num)
        l.append(row)
    return l

def add(m1,m2):
    result=[]
    for i in range(len(m1)):
        row=[]
        for j in range(len(m1[0])):
            row.append(m1[i][j]+m2[i][j])
        result.append(row)
r1=int(input("Enter the number of rows  of first matrix: "))
c1=int(input("Enter the number of colomns in first matrix : "))
r2=int(input("Enter the number of rows  of second matrix: "))
c2=int(input("Enter the number of colomns in second matrix : "))

if r1!=r2 or c1!=c2:
    print("Invalid dimensions")
else:
    print("Enter first matrix : ")
    m1=take_matrix(r1,c1)
    print("Enter second matrix : ")
    m2=take_matrix(r2,c2)
    display(m1)
    print("\n\n")
    display(m2)
    add_result=add(m1,m2)
    print("The sum matrix is ; ")
    display(add_result)
    print("The difference matrix is  : ")
    sub_result=sub(m1,m2)
    display(sub_result)
"""
