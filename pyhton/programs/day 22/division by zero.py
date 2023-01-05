#creat a function tkes alist as parameter and in the list you should have number
#as eg: 12,3,0,2. inside the function, you need to divide a number taken from the user
#by every number in the list. i.e the list numbers should be in the denominator
# if ther is division by zero you need to handle the exception


def divide(l,n):
    for i in l:
        try:
            print(n/i)
        except ZeroDivisionError as e:
            print("exceptioin occured",e)

            
l=list(map(int,input("enter the number by comma: ").split(",")))
n=int(input("enter number to be divided: "))
divide(l,n)
    
