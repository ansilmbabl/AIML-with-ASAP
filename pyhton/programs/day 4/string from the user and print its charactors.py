#WAP to get a string from the user and print its charactors

a= input("enter something : ")


print("method 1")
#i as an integer
for i in range(len(a)):
    print(a[i])

print("method 2")
#i as a charactor
for i in a:
    print(i)

