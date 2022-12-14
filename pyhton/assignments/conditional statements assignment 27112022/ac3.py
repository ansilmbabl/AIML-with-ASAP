x=int(input("enter the time in hour : "))

if x>=0 and x<=23:
    if x <= 5:
        print("night")
    elif x <= 11:
        print("morning")
    elif x <= 17:
        print("afternoon")
    else:
        print("evening")
else:
    print("invalid")
