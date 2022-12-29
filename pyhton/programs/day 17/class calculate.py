#create a class claculate which has a method add().
#if strings are passed into it, it will concatinate and return the string
#if numbers are passed into it, it will add the numbers and return the sum


class calculate:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        if self.a == "int":
            sum =0
            for i in self.b:
                sum+=i
            return sum
        else:
            sum=""
            for i in self.b:
                sum+=i
            return sum

obj1=calculate("int",[1,2,3,4,56])
obj2=calculate("str",["hi","welcome"])
print(obj1.add())
print(obj2.add())


