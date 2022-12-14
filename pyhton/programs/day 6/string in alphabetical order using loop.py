#WAP to get a string from the user and convert it into lowecase
#print the string in alphabetical order using loop

s=input("enter the string: ")
s.lower()

l=[]
for i in s:
    l.append(i)
    l.sort()

x=""
for i in l:
    x+=i
    
print(x)

