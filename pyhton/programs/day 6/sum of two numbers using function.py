#WAP to find the sum of two numbers using function

def total():
    global n1
    global n2
    n1=int(input("enter number1 :"))
    n2=int(input("enter number2 :"))

    print ("sum : ", n1+n2)
total()

print(n2)
n2=87
print(n2)

"""
anothet way
"""

def total2():
    print("sum : ",n1+n2)
    
n1=int(input("enter number1 :"))
n2=int(input("enter number2 :"))
total2()

"""
anothet way(general  purpose fn)
positonal arguiment (no: of arguiments=no: of positions)
"""

def total(a,b):
    print("sum : ",a+b)

a=int(input("enter number1 :"))
b=int(input("enter number2 :"))
total(a,b)

"""
anothet way(general  purpose fn)
default arguiment
"""

def total(a,b,c=0):
    print(a+b+c)
total(2,3,5)
total(2,3)

"""
varible length arguiment
"""

def total(a,b,*c):
    ----
    --------
total(1,2,3)
total(1,2,3,5,6,4,8,96,7)





























