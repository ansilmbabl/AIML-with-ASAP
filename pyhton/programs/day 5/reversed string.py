#WAP to get a string from the user and print it in reverse order using while loop

s=input("enter something : ")
a=len(s)-1

while a >= 0:
    print(a,end="")
    a-=1
