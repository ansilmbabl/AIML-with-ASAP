#WAP to take a number between 1 and 7 from the user

n = int(input("type a number between 1 to 7: "))

if n > 7 or n < 1:
    print(" ohohhh it's a wrong pick")
else:
    if n==1:
       print("You got Sunday")
    elif n==2:
       print("You got monday")
    elif n==3:
       print("You got tuesday")
    elif n==4:
       print("You got wednesday")
    elif n==5:
       print("You got thursday")
    elif n==6:
       print("You got friday")
    else:
       print("You got Saturday")
