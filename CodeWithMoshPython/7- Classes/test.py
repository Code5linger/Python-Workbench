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
"""

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
"""
# 6
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point = Point(1, 2)
print(point)
"""
# 7
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point < other)
"""
# 8
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined.x)
"""
# 9
"""

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud['python'] = 10
len(cloud)
cloud.add('Python')
cloud.add('python')
cloud.add('python')
print(cloud.tags)
"""
# 10
"""

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
print(cloud._TagCloud__tags)
"""
# 11
"""

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self.__price = value


product = Product(-100)
product.price = 2
print(product.price)
"""
# 12
"""

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')

# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')

m = Mammal()
m.eat()
print(m.age)
"""
# 13
"""

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print('walk')


m = Mammal()
print(isinstance(m, object))
print(issubclass(Mammal, object))
"""
# 14
"""

class Animal:
    def __init__(self):
        print('Animal Cons')
        self.age = 1

    def eat(self):
        print('eat')


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def __init__(self):
        print('Mammal Cons')
        self.weight = 2
        super().__init__()

    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')


m = Mammal()
print(m.age)
print(m.weight)
"""
# 15
"""

class Animal:
    def eat(self):
        print('eat')


class Bird(Animal):
    def fly(self):
        print('Fly')


class Chicken(Bird):
    pass

"""
# 16
"""

class Employee:
    def greet(self):
        print('Employee Greet')


class Person:
    def greet(self):
        print('Personal Greet')


class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet()
"""
# 17


class InvalidOperationError(Exception):
    pass


class Strem:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Strem is Already Open')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Strem is Already Closed')
        self.opened = False


class FileSteam(Strem):
    def read(self):
        print("Reading Data from a File")


class NetworkSteam(Strem):
    def read(self):
        print("Reading Data from a Network")
