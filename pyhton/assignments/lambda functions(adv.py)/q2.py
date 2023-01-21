#Write a lambda function to find the index of all the elements of a list.

l = [1,2,3,4,5,6,7,8,9,10]

index = list(map(lambda x: l.index(x),l))
print(index)
