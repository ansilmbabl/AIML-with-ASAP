#WAP to get a list of country names from the user and print the names of alternate country names

a=[]
b=int(input("enter the number of country: "))

for i in range(b):
    n=input("enter the country: ")
    a.append(n)
print(a)

for i in range (0,b,2):
    print(a[i],end=" ")
    
