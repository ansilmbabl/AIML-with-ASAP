
def bstr(s):
    new=""
    for i in s:
        if i in a:
            new += i
            
        elif i == ")":
            if new[-1] == "(":
                new = new[0:len(new)-1]
            elif new[-1] == "{":
                print("False")
                break
            elif new[-1] == "[":
                print("False")
                break
            else:
                print("False")
                

        elif i == "}":
            if new[-1] == "{":
                new = new[0:len(new)-1]
            elif new[-1] == "(":
                print("False")
                break
            elif new[-1] == "[":
                print("False")
                break
            else:
                print("False")
               

        elif i == "]":
            if new[-1] == "[":
                new = new[0:len(new)-1]
            elif new[-1] == "(":
                print("False")
                break
            elif new[-1] == "{":
                print("False")
                break
            else:
                print("False")
                
    if new == "":
        print("True")


a="({["
s=input("enter stringcontains ( , ) , { , } and [ , ] : ")
bstr(s)



