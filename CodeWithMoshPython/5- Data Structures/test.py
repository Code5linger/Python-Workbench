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
