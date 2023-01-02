#Create an abstract class named Polygon, inside the Polygon create an abstract method called ‘sidesOfPolygon’.
#Create another class named Triangle which should inherit the Polygon class and print the number of sides in Triangle using the abstract method ‘sidesOfPolygon’. 
#Create another class named Pentagon which should inherit the Polygon class and print the number of sides in Polygon using the abstract method ‘sidesOfPolygon’. 
#Create another class named Hexagon  which should inherit the Polygon class and print the number of sides in Hexagon using the abstract method ‘sidesOfPolygon’. 
#Create another class named Quadrilateral  which should inherit the Polygon class and print the number of sides in Quadrilateral 
#using the abstract method ‘sidesOfPolygon’. Finally, print the output for all the classes

from abc import ABC,abstractmethod

class polygon(ABC):
    
    @abstractmethod
    def sidesOfPolygon(self):
        pass

class triangle(polygon):
    def sidesOfPolygon(self):
        print("trianlge has 3 sides")

class pentagon(polygon):
    def sidesOfPolygon(self):
        print("pentagon has 5 sides")

class hexagon(polygon):
    def sidesOfPolygon(self):
        print("hexagon has 6 sides")

class quadrilateral(polygon):
    def sidesOfPolygon(self):
        print("quadrilateral has 4 sides")


t=triangle()
t.sidesOfPolygon()

q=quadrilateral()
q.sidesOfPolygon()

p=pentagon()
p.sidesOfPolygon()

h=hexagon()
h.sidesOfPolygon()
