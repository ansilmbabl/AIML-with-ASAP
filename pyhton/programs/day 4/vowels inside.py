#WAP to get a string from the user and print the vowels inside it.

a= input("enter something : ")
b= "aeiouAEIOU"

print("method 1")
# without range fn
for i in a:
    if i in b:
        print(i)

print("method 2")
# with range fn
for i in range(len(a)):
    if a[i] in b:
        print (a[i])
