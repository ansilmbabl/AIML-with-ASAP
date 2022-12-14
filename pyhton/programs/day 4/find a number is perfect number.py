#WAP to find a number is perfect number
##sum of factors = number itself



n=int(input("enter the number: "))
s=0


for i in range(1,n):
    if n%i == 0:
        s+=i
if s == n:
    print(n , " is a perfect number")
else:
    print("not a perfect number")


#saving half of the iteration
    # n-> (n//2)
su=0

for i in range(1,(n//2)+1):
    if n%i == 0:
        su+=i
if su == n:
    print(n , " is a perfect number")
else:
    print("not a perfect number")
