#encapsulation

class employee:
    def __init__(self,name,salary):
        self._name=name #protected attribute
        self.__salary=salary #private attribute

    def __display(self): #private method
        print(f"Name: {self._name}\nSalary: {self.__salary}")

    def display2(self):
        self.__display()

emp=employee("abc",10000)
emp.display() #private method,cant access
emp.display2() #for private method

##cannot acess attributes directly with object in private mode, can acces with methods only
#print(emp.salary)
#print(emp.__salary)

print(emp.__dict__) #return a dictionary with current values(private/public)
print(emp._employee__salary) #python has no full encapsulation

