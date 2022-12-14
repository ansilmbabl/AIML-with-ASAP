#WAP to get a number list and find s

l=list(map(int,input("enter the number seperated by comma :").split(",")))

s=0
p=1

for i in l:
    s+=i
    p*=i

print (s,p)

##?????????
##for i in l:
##    s+=i
##    p*=i
##
##print (f"sum= {s} and product= {p}")
