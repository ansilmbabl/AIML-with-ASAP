#WAP to get a list of numbers from the user and get the
n=list(map(int,input("enter the numbers seperated by \",\""" :" ).split(",")))
x=n[0]
y=n[0]
for i in n:
    if i > x:
        x=i
    if i < y:
        y=i
print(f"the biggest number is {x} and the smallest number is {y}")
