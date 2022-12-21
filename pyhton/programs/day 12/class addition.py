#class addition

class add:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self):
        return self.x + self.y

n1=int(input("enter number 1: "))
n2=int(input("enter number 1: "))

c1=add(n1,n2)
print("sum: ",c1.sum())

##method 2
class add:
    def __init__(self):
        self.x=int(input("enter number 1: "))
        self.y=int(input("enter number 2: "))

    def sum(self):
        print("sum: " ,(self.x + self.y))


c1=add()
c1.sum()
