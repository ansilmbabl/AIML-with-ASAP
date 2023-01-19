class myclass:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        self.a = self.a +1
        return self.a
    
m = myclass()
itr = iter(m)

for i in range(10):
    print(next(itr))

