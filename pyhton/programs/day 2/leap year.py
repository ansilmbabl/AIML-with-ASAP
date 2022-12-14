#WAP to take an year from the user and print it is a leap year or not ?

##a=int(input("Enter the year : "))
##
##if a%400 == 0:
##    print("its a leap year")
##elif a%4 == 0 and a%100 != 0:
##    print("its a leap year")
##else:
##    print("its not a leap year")
    
'''
or
'''
a=int(input("Enter the year : "))

if a%400 == 0 or (a%4 == 0 and a%100 != 0):
    print("its a leap year")
else:
    print("its not a leap year")
