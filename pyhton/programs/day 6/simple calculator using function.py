#WAP to implement a simple calculator using function

def display():
    print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.remainder\n6.power")
    choice=int(input("enter ur choice 1 to 6: "))
    return choice
def takeinput():
    a=int(input("enter num : "))
    return
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def rem(x,y):
    return x%y
def powe(x,y):
    return x^y

while True:
    choice=display()
    n1=takeinput()
    n2=takeinput()
    if choice == 1:
        result = add(n1,n2)
    elif choice == 2:
        result = sub(n1,n2)
    elif choice == 3:
        result = mul(n1,n2)
    elif choice == 4:
        result = div(n1,n2)
    elif choice == 5:
        result = rem(n1,n2)
    elif choice == 6:
        result = powe(n1,n2)
    else:
        result = "invalid choice"
    print(result)

    s = "type Y to continue "
    if s == "Yy":
        continue
    else:
        print("exiting.....")
        




"""
techers version

def display():
    print("1. Addition\n2. Subtraction\n3. Multiplication \n4. Division \n 5. Remainder \n 6. Power ")
    choice=int(input("Enter your choice from 1 to 6 : "))
    return choice
def takeinput():
    n=int(input("Enter number : "))
    return n
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def remainder(x,y):
    return x%y
def power(x,y):
    return x^y


while True:
    choice=display()
    n1=takeinput()
    n2=takeinput()
    if choice==1:
        print(add(n1,n2))
    elif choice==2:
        print(subtract(n1,n2))
    elif choice==3:
        print(multiply(n1,n2))
    elif choice==4:
        print(divide(n1,n2))
    elif choice==5:
        print(remainder(n1,n2))
    elif choice==6:
        print(power(n1,n2))
    else:
        print("invalid choice ")
    s=input("Press y to continue, press any other key to exit : ")
    if s in "Yy":
        continue
    else:
        print("Exiting...")
        break
"""
