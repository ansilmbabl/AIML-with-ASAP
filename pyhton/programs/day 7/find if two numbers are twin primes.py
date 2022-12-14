#WAP to find if two numbers are twin primes
#prime number differ by two

def prime(x):
    flag = 0
    for i in range(2,(x//2)+1):
        
        if x%i == 0:
            flag=1
    if flag == 0:
        return True
    else:
        return False
      
def twin_p(x,y):
    if max(prime(x),prime(y)) - min(prime(x),prime(y)) == 2 and prime(x) == prime(y) == True:
        print("twin prime")
    else:
        print("not twin prime")
        
x=int(input("enter num 1"))
y=int(input("enter num 2"))
twin_p(x,y)

