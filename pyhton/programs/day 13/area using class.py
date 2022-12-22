#write a python class named ractangle by length and width and a method which will return the area

class rectangle:

    def __init__(self,leng,wid):
        self.l = leng
        self.w = wid

    def area(self):
        return self.l * self.w

l = int(input("enter length: "))
w = int(input("enter width: "))

rect1 = rectangle(l,w)
print("Area = ", rect1.area())
