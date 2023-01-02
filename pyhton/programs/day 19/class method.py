#class method

class employee:
    company="facebook"

    #instance method
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        
    #instance method
    def assign_email(self):
        return f"{self.first_name}{self.last_name}@{employee.company}.com".lower()

    #class method
    @classmethod
    def changeCompany(cls,comp_name):
        cls.company=comp_name

    #staticmethod
    @staticmethod
    def staticmethod(x,y):
        return max(x,y)
        print("this is a static method")
        

#class method
employee.changeCompany("Google")
print(emp1.assign_email())

emp2=employee("dave","tum")
print(emp2.assign_email())


