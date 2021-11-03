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
def increment(number, by):
    return number + by

print(increment(2, by=10))