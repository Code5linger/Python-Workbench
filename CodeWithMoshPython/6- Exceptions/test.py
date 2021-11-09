# 1
"""
numbers = [1, 2]
print(numbers[3])
"""
"""
age = int(input('Age: '))

print(age)
"""
# 2
"""
try:
    age = int(input('Age: '))
    print('You are ', age, ' Years Old')
except ValueError:
    print('Enter a number between 1 to 100. '
          'Unless you are Keanu Reeves')
else:
    print('Boring!')
print('Something')
"""
# 3
"""
try:
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('Enter a number between 1 to 100. '
          'Unless you are Keanu Reeves')
else:
    print('Boring!')
"""
# 4
"""
try:
    file = open('test.html')
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('Enter a number between 1 to 100. '
          'Unless you are Keanu Reeves')
else:
    print('Boring!')
finally:
    file.close()
"""
# 5
"""
try:
    with open('test.html') as file, open('test.py') as target:
        print('File Opened.')
        file.__enter__()
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('Enter a number between 1 to 100. '
          'Unless you are Keanu Reeves')
else:
    print('Boring!')
"""
# 6
"""

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Afawdw')
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""
