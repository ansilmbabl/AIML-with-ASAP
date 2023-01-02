
from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self,shape_name):
        self.shape_name = shape_name

    @abstractmethod
    def Draw(self):
        pass


class circle(shape):
    def __init__(self,name):
        super().__init__(name)
        
    def Draw(self):
        print("this is ",self.shape_name)


class rectangle(shape):
    def __init__(self,name):
        super().__init__(name)
        
    def Draw(self):
        print("this is ",self.shape_name)

c=circle("circle")
c.Draw()

r=rectangle("rectanlge")
r.Draw()
