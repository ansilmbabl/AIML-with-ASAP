#WAP to get a number and print factors of it.

n=int(input("enter the number: "))

for i in range(1,n+1):
    if n%i == 0 :
        print(i,end=",")
