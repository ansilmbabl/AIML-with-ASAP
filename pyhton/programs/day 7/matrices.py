#WAP to create a 3x3 matrics and print the eleemnts afterwards

l=[[1,2,3],[4,5,6],[7,8,9]]


c=int(input("columns: "))
r=int(input("rows: "))

l=[]
for i in range(r):
    row=list(map(int,input(f"enter row {i}: ").split(",")))
    l.append(row)
    
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print()
