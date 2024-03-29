"""
Use of map in lambda
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :
  map(fun, iter)

Parameters :
fun : It is a function to which map passes each element of given iterable. 
iter : It is a iterable which is to be mapped.

Returns :
Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
"""


l = [10,20,30,40,50]
newlist = tuple(map(lambda x:x*x,l))
print(newlist)
