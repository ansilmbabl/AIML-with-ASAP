#usual practice

l = [1,2,3,4,5]
for i in range(len(l)):
    print(i)
#or
for i in l:
    print(i)
    
#using iterators (we can create sequence without allocating memory)

l = [1,2,3,4,5] #iterable object

itr = iter(l) # iterator

# traverse to the next item
for i in itr:
    print(i)
