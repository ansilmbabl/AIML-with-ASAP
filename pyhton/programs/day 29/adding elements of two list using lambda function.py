#add the elements of two list using lambda (multiple lists)

l1 =[1,2,3,4,5]
l2 =[10,20,30,40,50]

l = list(map(lambda x,y:x+y ,l1,l2))
print(l)
