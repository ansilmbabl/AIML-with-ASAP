


a= list (map(int,input("enter employee id seperated by space: ").split(" ")))
a.append(a[0])


x=0
for i in range(len(a)-2):
    if (a[i]+a[i+1])%2 == 0:
        x=1
        
if x == 1:     
    print("start meeting")
else:
    print("meeting cancelled")
