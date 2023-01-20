def rev(s):
    for i in s[::-1]:
        yield i

s=''
for i in rev("python"):
    s+=i
print(s)
