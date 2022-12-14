a = int(input("enter the sides 1 of the traingle: "))
b = int(input("enter the sides 2 of the traingle: "))
c = int(input("enter the sides 3 of the traingle: "))

if a**2==b**2 + c**2 or a**2+b**2 == c**2 or a**2+ c**2 == b**2  :
    print("yes")
else:
    print("no")
