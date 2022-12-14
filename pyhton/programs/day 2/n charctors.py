#WAP to get a string from the user. Get a number n also. print upto n characters from
#beginning and n characters from end of string.

a=input("enter the word: ")
b=int(input("enter a number: "))

if (b >= 0) and (b < len(a)):
    print(a[:b] , a[-1:-b-1:-1])
else :
    print ("check the numnber entered")
