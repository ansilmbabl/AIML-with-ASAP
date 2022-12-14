#WAP to get a list of country names from the user and print the names whose lenght is grater than five

a=[]
b=int(input("enter the number of country: "))

for i in range(b):
    n=input("enter the country: ")
    if len(n) > 5:
        a.append(n)
print(a)
