#Write a lambda function to find the length of all the strings in a list.

l = ['sdgf','sadkjhf','aghsdfv','askdhf','sgjgdvf','ksjgh','ksugb','jawfvi']

length = list(map(lambda x:len(x),l))
print(length)
