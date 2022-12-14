def cost(u):
    c = 0
    if u<0 :
        ("enter correct unit")
    else:
        if u<=100:
            c= u*0
        elif u<=200:
            c= (u-100)*5
        elif u<=500:
            c= (u-200)*8 + 500
        else:
            c= (u-500)*10 + 2400 + 500
    return c

def display(c):
    print("total cost = ",c)






u=int(input("units :"))
display(cost(u))
