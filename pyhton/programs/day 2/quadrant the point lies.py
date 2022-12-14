#WAP to take coordinate values of a point from the user and print in which quadrant the point lies

x = float(input("x = "))
y = float(input("y = "))

if x>0 and y>0:
    print ("it is in 1st quadrant")
elif x<0 and y>0:
    print ("it is in 2nd quadrant")
elif x<0 and y<0:
    print ("it is in 3rd quadrant")
elif x>0 and y<0:
    print ("it is in 4th quadrant")
elif x==0:
    print ("it is on x axis")
elif y==0:
    print ("it is on y axis")
else :
    print ("it is in origin")
