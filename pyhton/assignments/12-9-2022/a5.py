def encrypt(s):
    new=""
    for i in s:
        if i in al:
            x = al[-(al.index(i)+1)]
            new += x
        elif i in c_al:
            x = c_al[-(c_al.index(i)+1)]
            new += x
        elif i in n:
            x = n[-(n.index(i)+1)]
            new += x
        elif i == " ":
            new += "_"
        else:
            new += i
    print(new)




al="abcdefghijklmnopqrstuvwxyz"
c_al=al.upper()
n="0123456789"

s=input("enter string: ")

encrypt(s)
