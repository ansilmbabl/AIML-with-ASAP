class calculator:
    
    def sum(self,a,b):
        return("a+b = ", a+b)

    def multiply(self,a,b):
        return("a*b = ", a*b)

    def subtraction(self,a,b):
        return("a-b = ", a-b)

    def division(self,a,b):
        return("a/b = ", a/b)

    def remainder(self,a,b):
        return("a%b = ", a+b)

    def power(self,a,b):
        return("a**b = ", a**b)

    def quotient(self,a,b):
        return("a//b = ", a//b)


a = int(input("enter value for a: "))
b = int(input("enter value for b: "))

x = Calculator()

print(x.um(a,b))
print(x.Multiply(a, b))
print(x.Subtraction(a, b))
print(x.Division(a, b))
print(x.Remainder(a, b))
print(x.Power(a, b))
print(x.Quotient(a, b))
