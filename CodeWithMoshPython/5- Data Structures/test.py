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
numbers = [1, 2, 3, 1, 2, 3, 9]
first, second, *other, last = numbers
print(first, last)
print(second)
print(other)
"""
first = numbers[0]
second = numbers[1]
third = numbers[2]

print(first, second, third)
"""