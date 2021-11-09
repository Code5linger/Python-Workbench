# 1
"""
x = '1.0'
print(type(x))
"""
# 2
"""
class Point:
    def draw(self):
        print('draw')

point = Point()
print(type(point))
print(isinstance(point, Point))
"""
# 3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point(1, 2)
point.draw()

another = Point(3, 4)
another.draw()