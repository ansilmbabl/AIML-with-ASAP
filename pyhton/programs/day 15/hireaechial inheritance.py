#hireaechial inheritance

class Parent:
    m="moth"
    f="fath"

    def print_details(self):
        print("father is : ",self.f)
        print("mother is : ",self.m)

class child1(Parent):
    c1="child 1"

    def print_details(self):
        #calling parent method explicitly
        Parent.print_details(self)
        print("first child : ",self.c1)

class child2(Parent):
    c2="child 2"

    def print_details(self):
        Parent.print_details(self)
        print("second child : ",self.c2)


##objects

first_child=child1()
first_child.print_details()
print()

second_child=child2()
second_child.print_details()
