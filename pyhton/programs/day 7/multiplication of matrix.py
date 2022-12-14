#WAP to find the multiplication of matrix


def mat(r,c):
    l=[]
    for i in range(r):
        print("enter row : ",i)
        row=[]
        for j in range(c):
            num = int(input("enter column value : "))
            row.append(num)
        l.append(row)
    return l

def display(l):
    for i in range(len(l)):
        for j in range(len(l[0])):
            print(l[i][j],end=" ")
        print()

def mul(m,n):
    result=[]
    for i in range(len(m)):
        row=[]
        for j in  range(len(m[0])):
            sum=0
            for k in range(len(m[0])):
                mvalue = (m[i][k] * n[k][j])
                sum += mvalue
            row.append(sum)
        result.append(row)
    return result
    


r1=int(input("rows of matrics 1:"))
c1=int(input("columns of matrics 1:"))
r2=int(input("rows of matrics 2:"))
c2=int(input("columns of matrics 2:"))



if c1!=r2:
    print("cannot be multiplied")
else:
    print(">>>> first matrix")
    m = mat(r1,c1)
    
    print(">>>> second matrix")
    n = mat(r2,c2)
    print("\n")
    
    display(m)
    print("\n")
    display(n)

    mul(m,n)
    print(">>>>> multiplied matrix :")
##    display(mul(m,n))
    display(result)
