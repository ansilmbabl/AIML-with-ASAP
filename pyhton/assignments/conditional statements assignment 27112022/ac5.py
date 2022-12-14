


x=input("enter the password : ")

if len(x)>7 and len(x)<33:
    a=x[0]
    if a.isalpha() == True:
        if "/" or "\"" or "=" or " " or "\'" or "\\" in x:
            print("not a valid password")
        else:
            print("valid password")
    else:
        print("not a valid password")
else:
    print("not a valid password")
