
#programme
try:
    a=int(input("number 1: "))
    b=int(input("number 2: "))
    result = a/b

#errors that can be occured
except ValueError as e: 
    print("Excepation occured ",e)
except ZeroDivisionError as e:
    print("Excepation occured ",e)
except TypeError as e:
    print("Excepation occured ",e)
except:
    print("some problem occured")
    print("done")
else:
    print("result= ",result) #if try doeasnt have any problem
finally:
    print("completed.......") #final words(always will be printed)
    
