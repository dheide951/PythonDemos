
import math

class Apple:
    def __init__(self, color, size, sour, sweet):
        self.color = color
        self.size = size
        self.sour = sour

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

cir = Circle(5)
print(cir.area())

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (0.5)*(self.base * self.height)


tri = Triangle(10, 5)
print(tri.area())

class Hexagon:
    def __init__(self, sideLength):
        self.sideLength = sideLength

    def perimeter(self):
        return self.sideLength * 6

hexa = Hexagon(5)
print(hexa.perimeter())
        


