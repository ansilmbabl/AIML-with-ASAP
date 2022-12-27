#create class named employee having the following members id and name
#another class named hourlyemployee should have the datamembers hours waorked and hour rate
#another class named calculate payroll inherit both the employee and hourle emoployee classes
#payroll = number of hour worked * hour rate

class Employee:
    def __init__(self,i_d,name):
        self.i_d = i_d
        self.name= name

class HourlyEmployee(Employee):
    def __init__(self,i_d,name,hours_worked,hour_rate):
        Employee.__init__(self,i_d,name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

class CalculatePayroll(HourlyEmployee):
    def __init__self(self,i_d,name,hours_worked,hour_rate):
        HourlyEmployee.__init__(self,i_d,name,hours_worked,hour_rate)
        self.salary = ""

    def payroll(self):
        return self.hours_worked * self.hour_rate
        


e1= CalculatePayroll(21,"ans",1000,50)
print (f"{e1.name}\t{e1.i_d}\t{e1.hours_worked}\t{e1.hour_rate}\t{e1.payroll}")

