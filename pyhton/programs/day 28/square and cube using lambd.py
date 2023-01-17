l = list(map(int,input("enter numbers seperated by comma: ").split(",")))

square = list(map(lambda x : x*x,l)) #output in list
cube = tuple(map(lambda x : x*x*x,l)) #ouput in tuple

print(square)
print(cube)
