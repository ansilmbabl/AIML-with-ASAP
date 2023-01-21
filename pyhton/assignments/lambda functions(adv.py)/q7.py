#Write a Python program to count the even, odd numbers in a given array of integers using Lambda.

l = [1,2,3,4,5,6,7,8,9,0,15,623,9,62,59,6,63,65246]

count_odd = len(list(filter(lambda x: x%2!=0 ,l)))
count_even = len(list(filter(lambda x: x%2==0 ,l)))

print(count_odd)
print(count_even)

