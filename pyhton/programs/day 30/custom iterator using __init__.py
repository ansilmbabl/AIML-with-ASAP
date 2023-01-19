#without __init__
class square:
    
    def __iter__(self):
        self.n = 1
        return self
    def __next__(self):
        s = self.n**2
        self.n = self.n+1
        return s
    
obj = square()
itr = iter(obj)
for i in range(20):
    print(next(itr))
    
#with __init__
class square:
    
    def __init__(self,num):
        self.a = num
        
    def __iter__(self):
        return self
    
    def __next__(self):
        s = self.a**2
        self.a += 2
        return s
    
obj = square(2)

itr=iter(obj)
for i in range(10):
    print(next(itr))
