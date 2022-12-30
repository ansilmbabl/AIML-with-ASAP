class student_result:
    count=0

    def __init__(self,Roll_no,Student_name,Math,Physics,Chemistry,Computer,English,Email_id=None):
        student_result.count+=1
        self.Roll_no=Roll_no
        self.Student_name=Student_name
        self.Math=Math
        self.Physics=Physics
        self.Chemistry=Chemistry
        self.Computer=Computer
        self.English=English
        self.Email_id=Email_id

    def Average_marks(self):
        return ((self.Math + self.Physics + self.Chemistry + self.Computer + self.English)/5)

    def Total_marks(self):
        return (self.Math + self.Physics + self.Chemistry + self.Computer + self.English)

    def Max_marks(self):
        return max (self.Math,self.Physics,self.Chemistry,self.Computer,self.English)

    def Min_marks(self):
        return min (self.Math,self.Physics,self.Chemistry,self.Computer,self.English)

    def Display(self):
        print(f"{self.Roll_no} {self.Student_name} {self.Math} {self.Physics} {self.Chemistry} {self.Computer} {self.English} {self.Email_id}")

n=int(input("number of students: "))
for i in range(0,n):
    a = input("Roll number")
    b = input("Name")
    print("marks")
    c = int(input("Maths"))
    d = int(input("Physics"))
    e = int(input("Chemistry"))
    f = int(input("Computer"))
    g = int(input("English"))
    h = input("mail id")
    s=student_result(a,b,c,d,e,f,g,h)
    s.Display()
    print(s.Student_name,s.Total_marks(),s.Average_marks(),s.Max_marks(),s.Min_marks())

print('Total Students =',student_result.count)

