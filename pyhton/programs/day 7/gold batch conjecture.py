#Every even number greater than 2 is a sum of any two prime numbers
#gold batch conjecture

##def even(x):
##    if x%2 == 0:
##        return x


def prime(x):
    for i in range(2,(x//2)+1):
        flag = 0
        if x%i == 0:
            flag = 1
    if flag == 0:
        return True


n=int(input("enter even number >2 : "))
if n<=2 or n%2!=0:
    print("Invalid number " )
else:
    primes=[]
    for i in range(2,n):
        if checkprime(i)==True:
            primes.append(i)
   print(primes)
    for i in primes:
        if n-i in primes:
           print((i,n-i))
            primes.remove(i)

