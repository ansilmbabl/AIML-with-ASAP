"""
Question 4
write a programme to find maximum number in a list using lambda function
"""
from functools import reduce

l = list(map(int,input("enter the numbers: ").split(",")))

maxim = reduce(lambda x,y: x if x>y else y,l)
# or
# maxim = reduce(lambda x,y: max(x,y),l)
print(maxim)
