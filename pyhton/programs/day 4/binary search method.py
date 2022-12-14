#WAP to search a number in a list using binary search method

'''
n=list(map(int,input("enter the numbers seperated by \",\""" :" ).split(",")))
n.sort()
key=int(input("enter the number to be found : "))

low = 0
high = key
mid = (low + high)//2
flag = 0

for i in n:
    if i==key:
        flag = 1
        print("number exist")
        break
    if key > i:
        low = i
        high = mid
    if key < i:
        low = mid
        high = i
if flag == 0:
    print("number does not exist")
'''      
## here value of element is found (not binary search method) but need to go with its position
# teachers method

l=list(map(int,input("enter the numbers seperated by \",\""" :" ).split(",")))
n=len(l)
low =0
high = n-1
flag=0
num=int(input("enter the number to be found : "))
l.sort()

for i in range(n):
    mid=(high + low)//2
    if l[mid] > num:
        high = mid -1
    elif l[mid]<num:
        low=mid+1
    elif l[mid]==num:
        flag=1
        print(f"{num} is found at {mid}")
        break
if flag == 0:
    print(f"{num} is not found")
