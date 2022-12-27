#single inheritance

class Parent:
        m=""
        f=""

class child(Parent):
    c=""
    def print_details(self):
        print("mother name is : ", self.f)
        print("mother name is : ", self.m)
        print("child name is : ", self.c)

child1=child()
child1.f="xyz"
child1.m="pqr"
child1.c="abc"
child1.print_details()
