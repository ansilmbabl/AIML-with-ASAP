# without using lambda functon
l=[("A",32),("B",21),("C",25),("D",20),("E",35)]

#without using lambda functon
def second_item(a):
    return a[1]
l = sorted(l,key = second_item)
print(l)

#with lambda functon
q = sorted(l,key = lambda y:y[1])
print(q)
