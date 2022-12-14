#recursive function

def search(l,n):
    if len(l)==0:
        False
    if n==l[0]:
        return True
    else:
        return search(l[1:],n)

l=list(map(int,input("enter a lsit by comma : ").split(",")))
n=int(input("enter the number to be found : "))

if search(l,n) == True:
    print("item found")
else:
    print("not found")
