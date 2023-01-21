#Write a Python program that removes the positive numbers from a given list of numbers. Sum the negative numbers and print the absolute value using lambda function. Print the result.

from functools import reduce
l = [1,2,-654,55,51,-46,-4,-86,12,-7,23,315,-4]

sum = reduce(lambda x,y:x+y, list(filter(lambda x: x<0,l)))
print(sum)
