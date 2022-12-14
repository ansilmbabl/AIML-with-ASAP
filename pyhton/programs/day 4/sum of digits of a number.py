#WAP to find sum of the digits of a number

sum=0

'''
method 1

n=input("enter the number: ")
for i in n:
    sum+=int(i)
print sum

method 2
'''

n=int(input("enter the number: "))
num = len(str(n))

for i in range (num):
    sum += (n%10)
    n = n//10
print(n)
