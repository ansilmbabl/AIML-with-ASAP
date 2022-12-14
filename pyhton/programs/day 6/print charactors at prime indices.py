#WAP to get astring from the user and print charactors at prime indices:

s=(input("enter the searching: "))


##l=[]
##
##i=1
##while i < len(s):
##    for j in range(2,i):
##       if i%j == 0:
##           l.append(i)
##    i+=1
##    break
##print(l)



##for i in range(2:):
##    if i%2
##    
##while len(s)>len(l)

for i in range (2,len(s)):
    flag=0
    for j in range(2,(i//2)+1):
        if i%j == 0:
            flag=1
            break
    if flag==0:
        print(s[i],end="")
