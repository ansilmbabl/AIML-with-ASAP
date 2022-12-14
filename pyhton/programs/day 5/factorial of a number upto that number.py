#WAP to get a number from the user. Print factorial of all numbers upto that number

n=int(input("enter the number: "))
##p=1
for i in range(1,n+1):
    a=1
    for j in range (1,i+1):
        a=a*j
    print(f"factorial {a}")
##    p = p*i
##    print(f"{i} factorial {p}")
