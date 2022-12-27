#hireaechial inheritance seperate methods for parent and child

class Parent:
    m=input("mother name : ")
    f=input("father name : ")

    def print_par_details(self):
        print("father is : ",self.f)
        print("mother is : ",self.m)

class child1(Parent):
    c1=input("child 1 name : ")

    def print_details(self):
        #calling parent method explicitly
        self.print_par_details()
        print("first child : ",self.c1)

class child2(Parent):
    c2=input("child 2 name : ")

    def print_details(self):
        self.print_par_details()
        print("second child : ",self.c2)


##objects

first_child=child1()
first_child.print_details()
print()

second_child=child2()
second_child.print_details()
