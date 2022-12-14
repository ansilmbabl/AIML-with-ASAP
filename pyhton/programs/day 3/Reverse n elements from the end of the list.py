#WAP to take a number n from the user. Reverse n elements from the end of the list

n = int(input("enter the number : "))

l = [1,2,3,4,5,6,7,8,9,10]
l1= l[0:-n]
l2= l[len(l):-n-1:-1]
print(l1)
print(l2)
##l1.extend(l2)
##print(l1)
l3=l1+l2
print(l3)









##l3= l1.extend(l2)
##print(type(l1))
##print(type(l2))
##print(type(l3))

