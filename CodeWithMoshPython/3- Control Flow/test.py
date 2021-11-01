# 2
"""
temp = 0
if temp > 30:
    print('Hot🔆')
elif temp > 20:
    print("cold❄")
else:
    print("No Idea")
print("Done")
"""
# 3
"""
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

# message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
"""
# 4
"""
high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Ka-ching 🤑")
else:
    print("Go Fish🐟")
"""
# 6
"""
age = 220
if 18 <= age < 65:
    print('Ok')
else:
    print('Too Old')
"""
# 7
"""
if 10 == "10":
    print('a')
elif 'bag' > 'apple' and 'bag' > 'cat':
    print('b')
else:
    print('c')
"""
# 8
"""
for number in range(1, 10, 1):
    print('Attempt', number, number + 1, (number + 1) * '.')
"""
# 9
"""
successful = False
for number in range(3):
    print('Attempt')
    if successful:
        print('Sucessful')
        break
else:
    print('Attempted 3 times and failed!')
"""
# 10
"""
for x in range(5):
    for y in range(2):
        print(f"({x}, {y})")
"""
# 11
"""
print(type(5))
print(type(range(7)))
"""
'''
for x in range(5):
    print(x)
'''
"""
for x in 'CodeSlingr':
    print(x)
"""
"""
for x in [1, 2, 3, 4]:
    print(x)
"""
"""
shopping_cart = ["book", "pen", "notebook"]
for items in shopping_cart:
    print(items, 'is in the cart🛒')
"""
# 12
"""
number = 100
while number > 0:
    print(number)
    number //= 2
"""
"""
command = ""
while command.lower() != 'quit':
    command = input(">")
    print("ECHO", command)
"""
