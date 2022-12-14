#WAP to create a list of multiples of 3 from 6 to 30 and print double of each element in the list

a= list(range(6,31,3))
print (a)

print ("without range")
for i in a:
    print(i*2,end=" ")


print ("\nwith range")
for i in range(len(a)):
    print(a[i]*2,end=" ")
    
