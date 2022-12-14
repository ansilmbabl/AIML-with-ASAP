#WAP to get a list of number and count the even number

n=list(map(int,input("enter the numbers seperated by \",\""" :" ).split(",")))
x=0

for i in n:
    if i%2==0:
        x+=1
print(x)
