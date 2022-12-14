#WAP to print if a number is prime number or not
#3,3,7,11........

n=int(input("enter the number : "))
flag=0

for i in range(2,(n//2)):
    if n%i == 0:
        flag=1
        print(n,"is not a prime")
        break
if flag==0:
    print(n,"is a prime")
