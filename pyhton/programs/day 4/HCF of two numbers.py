#WAP to find HCF of two numbers

n=int(input("enter the number 1: "))
m=int(input("enter the number 2: "))
hcf=1
for i in range(1,min(n,m)+1):
    if n%i == 0 and m%i == 0:
        if i > hcf:
            hcf=i
print("HCF = ",hcf)
