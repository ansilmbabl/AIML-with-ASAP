#Write a Python program to filter a list of integers using Lambda.

l = [1,2.0,5,3.6,4.5,1.0,8,45,26,9.2,4.6,54,0.32]

filtered = list(filter(lambda x: type(x)==int ,l))
print(filtered)
