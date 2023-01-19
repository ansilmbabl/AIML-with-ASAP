#with return 
def func():
    print("hello")
    return 1
    return 2
    print("hi")
print(func())

#with yield (generator)
def genfun():
    print("hello")
    yield 1
    yield 2
    print("hi")
    yield 3
    
count = 0
for val in genfun():
    count+=1
    print(val)
print("count = ",count)
