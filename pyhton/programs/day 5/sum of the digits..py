#WAP to get a number from the user and find the sum of the digits.

a=int(input("enter number : "))
s=0

while a > 0:
    num = a%10
    s = s + num
    a = a//10
print(s)
