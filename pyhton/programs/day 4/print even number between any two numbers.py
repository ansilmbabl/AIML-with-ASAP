#WAP to print even number between any two numbers taken from the user

a= int(input("number 1: "))
b= int(input("number 2: "))

for i in range(a,b+1):
    if i%2 == 0:
        print(i,end=",")
