#accept two strings from the user
#remove all the charctors from the second string which are present in the first string

s1=(input("enter the string1: "))
s2=(input("enter the string2: "))

x=""
for i in s2:
        if i not in s1:
            x+= i
print(x)



