#WAP using classes and object to take the employee name ,salary , absent days as input and calculate the total salary after dedcting the LOP of the employee and disaply it . asume month has 30 days 


class salary:
    count=0
    def __init__(self):
        salary.count+=1
        self.n = ""
        self.s = ""
        self.ab= ""
        

    def emp(self):
        print("employee ",salary.count)
        self.n = input("name : ")
        self.s = int(input("salary per month : "))
        self.ab= int(input("number of days absent : "))
        
        
    def sal(self):
        return (self.s - self.ab * int((self.s/30)) )

    def details(self):
        print(f"{self.n}\t{self.s}\t{self.ab}\t{self.sal()}")


nu = int(input("number of employees: "))
l=[]


for i in range(nu):
    e = salary()
    l.append(e)
    l[i].emp()
    l[i].sal()

print("employee detail: ")
print("name\tsalarypm\tabsent\tsalary")

for i in l:
    i.details()
