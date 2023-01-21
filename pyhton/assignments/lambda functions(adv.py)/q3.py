#Write a lambda function to add two lists.

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [9,8,7,6,5,4,3,2,1]

added = list(map(lambda x,y:x+y,l1,l2))
print(added)
