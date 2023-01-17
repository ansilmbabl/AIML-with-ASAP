"""
Question 2
write a programme to get a list of strings from the user and convert each string to uppercase using lambda functions

"""
s = list(input("enter the names : ").split(","))
u = list(map(lambda x:x.upper(),s))
print(u)


"""
Question 3
print strings from above whose lenght ia greater than 3 using lambda
"""

newlist = filter(lambda x:len(x)>3,s)
list(newlist)
