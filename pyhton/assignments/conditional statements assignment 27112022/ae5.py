#5. Accept three positive integers from the user, and check if they form sides of a right angled triangle

a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
c=int(input("enter number 3: "))


if (a*a == b*b + c*c) or (a*a + b*b == c*c) or (b*b == a*a + c*c) :
    print ("sides of a triangle")
else:
    print ("not the sides of a triangle")
