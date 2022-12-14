#2. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

b = .05
s = int(input("enter salary : "))
y = int(input("enter year of service : "))

if y > 5:
    s+= (s*b)
    print(s)
else:
    print (s)
