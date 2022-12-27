#single inheritance with costructor

class Parent:
    def __init__(self,m,f):
        self.m=m
        self.f=f

class child(Parent):
    def __init__(self,c,f,m):
        self.c=c
        #Parent.__init__(self,m,f)
        #or
        super().__init__(m,f)
    def print_details(self):
        print("father name is : ", self.f)
        print("mother name is : ", self.m)
        print("child name is : ", self.c)

child1=child("xyz","fath","moth")
child1.print_details()
