#WAP to get a list of numbers from the users and search for first occurence of a number in it

l = list(map(int,input("enter the numbers by comma : ").split(",")))
key=int(input("enter the number to be found : "))

flag = 0
for i in l:
    if i == key:
        flag=1
        print(key,"found")
        break
if flag==0:
    print(key,"not found")
