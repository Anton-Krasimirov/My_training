import math # коренквадратен от: (x2 - x1)**2 + (y2 - y1)**2 - Distance between two points
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, a):
        self.x = a

    def set_y(self, b):
        self.y = b

    def distance(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
