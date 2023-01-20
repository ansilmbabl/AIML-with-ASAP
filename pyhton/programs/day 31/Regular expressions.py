###Regular expressions

s= 'i am born in 9-12th of 2020'
x = re.findall("\d",s) 
print(x)
y = findall("\w",s)
print(y)
z = findall("\s",s)
print(z)
p = findall("\S",s)
print(p)

q=len(findall("n",s))
print(q)

##search
x=search("\d",s)
print(x)
y=search("born",s)
print(y)
z=search("abcd",s)
print(z)

print(x.string)
print(x.span())
print(x.group())

p = search("\s",s)
if p:
    print("whitespace present")
else:
    print("whitespace not present")
    
## split()
x=split(" ",s)# refular expression
print(x)

y=s.split(" ") #split method
print(y)

# sub
w=sub("\s","*",s)
print(w)
a= input("enter somthing")
q= sub('\s',f"[{a}",s)
print(q)
