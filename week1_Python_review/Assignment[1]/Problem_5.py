import math
class Shape:
    def __init__(self, name):
        self.name = name

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def compute_area(self):
        self.area = math.pi * (self.radius**2)
        return self.area

    def compute_perimeter(self):
        self.perim = 2 * math.pi * self.radius
        return self.perim
        

class Rectangle(Shape):
    def __init__(self, name, length, height):
        super().__init__(name)
        self.length = length
        self.height = height
        

    def compute_area(self):
        self.area = self.length * self.height
        return self.area

    def compute_perimeter(self):
        self.perim = 2 * (self.length + self.height)
        return self.perim

c = Circle("Moon", 15)
print(c.compute_perimeter())
r = Rectangle("Block", 20, 10)
print(r.compute_area())



