# 1
"""
letters = ['a', 'b', 'c']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
char = list('Hello World')
print(len(char))
"""
# 2
"""
letters = ['a', 'b', 'c', 'd']
letters[0] = 'Z'
print(letters[-1])
print(letters[0:3])
print(letters[::2])
"""
"""
numbers = list(range(20))
print(numbers[::-1])
"""
# 3
"""
numbers = [1, 2, 3, 1, 2, 3, 9]
first, second, *other, last = numbers
print(first, last)
print(second)
print(other)
"""
"""
first = numbers[0]
second = numbers[1]
third = numbers[2]

print(first, second, third)
"""
# 1 Re:
"""
letters = ['a', 'b', 'c']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list('Hello World!')
print(len(chars))
"""
# 2 Re:
"""
letters = ['a', 'b', 'c']
letters[0] = 'Z'
print(letters[0:2])
"""
"""
numbers = list(range(20))
print(numbers[::-1])
"""
# 3 Re:
"""
numbers = [1, 2, 3, 1, 2, 3, 9]
first, second, *other, last = numbers

print(first, second)
print(other)
print(last)

def multiply(*numbers):
    multiply(1, 2, 3)
"""
# 4
"""
letters = ['a', 'b', 'c']

for index, letter in enumerate(letters):
    print(index, letter)
"""
# 5
"""
letters = ['a', 'b', 'c', 'b']

# Add
letters.append('d')
letters.insert(0, '_')

# Remove
letters.pop(0)
letters.remove('b')
del letters[0:3]
letters.clear()
print(letters)
"""
# 6
"""
letters = ['a', 'b', 'c']
print(letters.count('a'))
if 'a' in letters:
    print(letters.index('a'))
"""
# 7 & 8
"""
numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)
"""
"""
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

items.sort(key=lambda item: item[1])
print(items)
"""
# 9
"""
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]


prices = list(map(lambda item: item[1], items))
print(prices)
for item in prices:
    print(item)
"""
# 10
"""
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
"""
# 11
"""
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)

# filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(filtered)
"""
# 12
"""
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip('abc', list1, list2)))
"""
# 13
"""
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session)
"""
# 14
"""
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print('empty')
"""
# 15
"""
point = sorted((1, 2) + (3, 4) * 3)
print(point)
"""
"""
point = (1, 2, 3)
print(point[0:2])
x, y, z = point
if 10 in point:
    print('exists')

point[0] = 10
"""
# 16
"""
x = 10
y = 11

z = x
x = y
y = z

print('x', x)
print('y', y)
"""
"""
x = 10
y = 11

x, y = y, x

print('x', x)
print('y', y)
"""
