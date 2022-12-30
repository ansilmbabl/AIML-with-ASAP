class student_result:

    def __init__(self,Roll_no,Student_name,Math,Physics,Chemistry,Computer,English,Email_id=None):
        self.Roll_no=Roll_no
        self.Student_name=Student_name
        self.Math=Math
        self.Physics=Physics
        self.Chemistry=Chemistry
        self.Computer=Computer
        self.English=English
        self.Email_id=Email_id

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
