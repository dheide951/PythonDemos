
class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.width*2) + (self.length*2)

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side*4

    def change_size(self, size):
        for x in range(4):
            self.side += size

class Horse:
    def __init__(self,rider):
        self.rider = rider

class Rider:
    def __init__(self,name):
        self.name = name

rider = Rider("Dawson")
horse = Horse(rider)

rect = Rectangle(10,5)
sqr = Square(5)

rect.what_am_i()
sqr.what_am_i()

print(rect.perimeter())
print(sqr.perimeter())


