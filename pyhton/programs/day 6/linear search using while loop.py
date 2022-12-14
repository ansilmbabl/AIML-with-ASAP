#WAP to implement linear search using while loop

l=list(map(int,input("enter element : ").split(",")))
key=int(input("enter the searching: "))


i=0
flag=0
while i < len(l):
    if l[i]==key:
        flag=1
        print(f"{key} found at position {i}")
        break
    i+=1
if flag==0:
    print(f"{key} not found in list")
