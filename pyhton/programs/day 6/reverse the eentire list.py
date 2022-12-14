#WAP to get a string list from the user , reverse each string in the list
#also reverse th eentire list

l=list(input("enter element : ").split(","))
print(l)
##k=[]
##
##for i in l:
##    for j in range(len(i)-1,0,-1):
##        x=""
##        j=0
##        while j < len(i)-1:
##            x+=i[j]
##            j+=1
##            
##        k.append(x)
##
##print(k)

t=[]
for i in range (len(l)-1,-1,-1):
    s=""
    for j in range(len(l[i])-1,-1,-1):
        s=s+l[i][j]
    t.append(s)
print(t)
