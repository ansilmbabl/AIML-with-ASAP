#WAP to get a string from the user and print the position of vowels

a= input("enter something : ")

for i in range(len(a)):
    if a[i] in "aeiouAEIOU":
        print (i,end=",")
