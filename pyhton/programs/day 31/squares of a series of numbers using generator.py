def square(n):
    for i in range(1,n):
        yield i*i

for x in square(11):
    print(x)
