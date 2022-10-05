# kind of unfair because I've seen this 1000 time in game dev
# but a vector type is super useful
# I'm overriding operator methods here: https://www.geeksforgeeks.org/operator-overloading-in-python/
class Vector:
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y


# I use these constants later
ZERO = Vector(0, 0)
RIGHT = Vector(1, 0)
LEFT = Vector(-1, 0)
UP = Vector(0, 1)
DOWN = Vector(0, -1)
