#WAP to get two numbers from the user and find LCM of the two numbers using for loop

n1=int(input("enter the number1: "))
n2=int(input("enter the number2: "))


for i in range (max(n1,n2),(n2*n1)+1,max(n1,n2)):
        if i%n1==i%n2 == 0:
            print ("LCM = ",i)
            break
        
