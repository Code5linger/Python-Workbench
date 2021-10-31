# Loops and Iteration
"""
n = 5
while n > 0:
    print(n)
    n = n - 1
print(n)
print('Blastoff!')
"""

'''
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')
'''
"""
for i in [5, 4, 3, 2, 1, 0]:
    print(i)
print("Blastoff🚀")
"""
"""
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year', friend, '🎆🎇')
print('Done!')
"""
"""
print('Before')
for thing in [9, 12, 41, 3, 17, 9, 12, 41, 3, 17,] :
    print(thing)
print('After')
"""
"""
largest_so_far = -1
smallest_so_far = 100
print('Before', largest_so_far)
for the_num in [9, 12, 41, 3, 17, 9, 12, 74, 41, 3, 99, 17, 0] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
    print('Biggest Yet ➡', largest_so_far)
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
    print('Smallest Yet ➡', smallest_so_far)
"""
"""
code = 0
sum = 0
print('Before', code)
for thing in [9, 41, 17, 25, 14]:
    code = code + 1
    sum = sum + thing
    print(code, thing)
print('After ➡', code)
print('Sum ', sum, 'Avg', sum/code)
"""
"""
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3 :
        found = True
        break
    print(found, value)
print('After', found)
"""
""" 
smallest_so_far = None
print('Before', smallest_so_far)
for value in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = value
    elif value < smallest_so_far:
        smallest_so_far = value
    print(smallest_so_far)
print('After', smallest_so_far)
"""
"""
tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)
"""
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)