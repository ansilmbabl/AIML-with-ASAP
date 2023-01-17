## tuple
# [(name, mark, age)]
l=[("A",32,11),("B",21,10),("C",25,11),("D",20,8),("E",20,9)]
q = sorted(l,key= lambda y:(y[2],y[1]))
print("ascending : ",q)

r = sorted(l,key= lambda y:(y[2],y[1]),reverse = True)
print("decsending: ",r)

## dictionary 
mylist = [{"name":"nadini","age":20},{"name":"manu","age":20},{"name":"nikhil","age":19}]
l = sorted(mylist, key = lambda x:(x["age"],x["name"]))
print("sorting based on two conditions: age and name")
print(l)
