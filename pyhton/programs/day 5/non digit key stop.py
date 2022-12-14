#WAP to inout a list of numbers . keep on taking untill the user presses a non digit key



##l=[]
##
##
##while a.isdigit() == True:
##    a=input("enter number : ")
##    l.append(a)
##    if a.isdigit() == False:
##        break
##
##print(l)


print("enter number, to stop press a non digit")

while True:
    n=input("enter number : ")
    if n.isdigit()!=True:
        break
    else:
        l.append(int(n))

print(l)
