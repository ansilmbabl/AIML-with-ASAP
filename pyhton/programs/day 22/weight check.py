#wap to handle the exception if anegative number os encountered in the list of
#tuples which has name and weight of a person .[("abc",40),("xyz",12)]

class weightError(Exception):
    def __init__(self,w):
        super().__init__(w)

def weightCheck(l):
    for i in l:
        if i[1] < 0:
            raise weightError(f"negative value entered for {i[0]}")

try:
    l=[]
    n=int(input("enter number people : "))
    for i in range(n):
        name = input("enter name: ")
        weight = int(input("enter weight: "))
        l.append((name,weight))

    weightCheck(l)
    

except weightError as e:
    print(e)

else:
    print(l)
