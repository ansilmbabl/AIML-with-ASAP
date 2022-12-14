#WAP to take two numbers from user
#print all prime numbers between those two numbers,iniclusive.

n1=int(input("enter the number 1 : "))
n2=int(input("enter the number 2 : "))

l=[]
flag=0
if n1 < n2:
    for i in range(n1,n2+1):
        for j in range (2,(i//2)+1):
            if i%j == 0:
                flag=1
                break
        if flag == 0:
                l.append(i)
    print(l)

elif n1 > n2:
    for i in range(n2,n1+1):
        for j in range (1,i//2):
            if i%j == 0:
                flag=1
                break
        if flag == 0:
                l.append(i)
    print(l)

else:
    print("the numbers are same ")


