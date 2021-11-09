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
"""

class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


Point.default_color = 'black'
point = Point(1, 2)
print(point.default_color)
print(point.default_color)
point.draw()

another = Point(3, 4)
another.draw()
"""
# 5


class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point.zero()
point.draw()
