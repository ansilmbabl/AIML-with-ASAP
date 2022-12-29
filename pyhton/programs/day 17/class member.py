#Create a class named 'Member' having the following members:
#Data members 1 – Name 2 – Age 3 - Phone number 4 – Address 5 - Salary
#It also has a method named 'printSalary' which prints the salary of the members
#Two classes 'Employee' and 'Manager' inherits the 'Member' class.
#The 'Employee' and 'Manager' classes have data members 'specialization' and
#'department' respectively. Now, assign name, age, phone number, address and
#salary to an employee and a manager by making an object of both of these classes
#and print the same.




class member:
    def __init__(self,name,age,ph_num,address,salary):
        self.name = name
        self.age = age
        self.ph_num=ph_num
        self.address=address
        self.salary=salary

    def print_salary(self):
        print(self.salary)


class employee(member):
    def __init__(self,specialisation):
        member.__init__(self,name,age,ph_num,address,salary)
        self.specialisation = specialisation

        ##or
##        details=[name,age,ph_num,address,salary]
##        super().__init__(*details)
##        self.specialisation = specialisation


class manager(member):
    def __init__(self,department):
        member.__init__(self,name,age,ph_num,address,salary)
        self.department = department

        ##or
##        details=[name,age,ph_num,address,salary]
##        super().__init__(*details)
##        self.department = department


