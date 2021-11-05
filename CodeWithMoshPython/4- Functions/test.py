# 2
"""
def greet(first_name, last_name):
    print('Yo yo yo!' + first_name + last_name)
    print(f"It's your boy! {first_name} {last_name}")

greet("Code", "Slinger")
greet("Sakib", " ")
"""
# 3
"""
def greet(name):
    print(f"Hi {name}")
    return '...'

print(greet("Code"))

def get_greeting(name):
    return f"Hi there {name}"

message = get_greeting("Code")
file = open('content.txt', 'w')
file.write(message)
"""
# 4
"""
def increment(number = 23,by = 7):
    return number + by

print(increment(9, 1))
"""
# 6
"""
def multiply(*numbers):
    print(numbers)

multiply(2, 3, 4, 5)
"""
# 1 Re:
"""
def greet(name = 'Slinger🔫'):
    print('Hi!' + name)
    print('Welcome😊')

greet('Code')
"""
# 2 Re:
"""
def greetings(first_name="Nemo", last_name="XX"):
    print('Welcome ' + 'Mr. ' + first_name)
    print(f'We are glad you are here.{first_name} {last_name}')


greetings('Code', 'Slinger')
greetings('Lorem', 'Ipsum')
greetings()
"""
# 3
"""
def greet(name):
    print(f'Hi {name}')
    return "..."

print(greet('Code'))
"""
# 4
"""
def increment(number, by=5):
    return number + by


print(increment(5))
"""
# 5
"""
def increment(number, by=5):
    print(number + by)
    return "-_-"


increment(2, 10)
"""
# 6
"""
def multipy(*numbers):
    total = 1
    for numbers in numbers:
        total *= numbers
    return total


print(multipy(6, 3, 4, 5, 9, 11))
"""
# 7
"""
def save_user(**user):
    print(user['id'])
    print(user['name'])


save_user(id=1, name='code', age=26)
"""
# 8
"""
message = 'x'

def greet():
    global message
    print(message)

print(greet())
"""
# 9


def multiply(*numbers):
    total = 1
    for numbers in numbers:
        total *= numbers
    return total


print('Start>')
print(multiply(2, 3, 4, 5, 6))
