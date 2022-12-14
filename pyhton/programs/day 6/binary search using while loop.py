#WAP to implement binary search using while loop

l=list(map(int,input("enter element : ").split(",")))
key=int(input("enter the searching: "))
l.sort()

low=0
high=len(l)-1
flag=0

while low<=high:
    mid = (low+high)//2
    if key<l[mid]:
        high=mid-1
    elif key>;[mid]:
        low=mid+1
    else:
        flag=1
        print(f"Found at postion {mid}")
        break
if flag==0:
    print("not found")
