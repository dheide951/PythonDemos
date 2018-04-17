
class Square:
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {}".format(self.side, self.side)

sqr = Square(10)
print(sqr)

def equals(ob1, ob2):
    return ob1 is ob2

