#ploymorphism
##method over loading

class ABC:
    def disp(self,a=None,b=None):
        if a==None:
            print("None")
        else:
            print(a)
            print(b)

obj=ABC()
obj.disp() #without passing argument
obj.disp("mrngzz","dfgh") #with passing argument
obj.disp("mrngzz")
