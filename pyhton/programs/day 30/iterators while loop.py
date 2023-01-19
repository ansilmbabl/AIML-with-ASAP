l=[1,2,3,4,5,6,7,8,9,10]
itr = iter(l)
while True:
    try:
        element = next(itr)
        print(element)
    except StopIteration:
        break
        
