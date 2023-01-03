##find the max ways in which the options of a multiple select answer type question can have
##note : atleast one option should be selected by the student


n=[] # possible answers
l=["x","x","x","x"] #options = [a,b,c,d]


# x -> not selected the option
# a -> selected the option a
# b -> selected the option b
# c -> selected the option c
# d -> selected the option d

a=["a","x"] 
b=["b","x"]
c=["c","x"]
d=["d","x"]


#selection of options
for i in a: #option a
    l[0]=i
    for i in b: #option b
        l[1]=i
        for i in c: #option c
            l[2]=i
            for i in d: #option d
                l[3]=i
                n.append(l)
                print (l)
                
n.remove(["x","x","x","x"]) # not selected any option
print("total number ways we have: ",len(n)) # total number ways we have


"""
output

['a', 'b', 'c', 'd']
['a', 'b', 'c', 'x']
['a', 'b', 'x', 'd']
['a', 'b', 'x', 'x']
['a', 'x', 'c', 'd']
['a', 'x', 'c', 'x']
['a', 'x', 'x', 'd']
['a', 'x', 'x', 'x']
['x', 'b', 'c', 'd']
['x', 'b', 'c', 'x']
['x', 'b', 'x', 'd']
['x', 'b', 'x', 'x']
['x', 'x', 'c', 'd']
['x', 'x', 'c', 'x']
['x', 'x', 'x', 'd']
['x', 'x', 'x', 'x']
total number ways we have:  15

"""
