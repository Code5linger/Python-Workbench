"""
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()
"""
"""
i = 42
print(i)
f = float(i)
print(f)

print(1 + 2 * float(3) / 4 - 5)
"""
"""
x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okey.")
    print("I sleep all night and I work all day.")

print('Yo')
print_lyrics()
x = x + 2
print(x)
"""
'''
name = input('What is your name? ')
gender = input('What\'s your gender? ')
lang = input('en es fr: ')
def greet(lang):
    if lang == 'es':
        return ('Hola!')
    elif lang == 'fr':
        return ('Bonjour')
    else:
        return ('Hello')
def address(gender):
    if gender == 'm':
        return ('Mr.')
    elif gender == 'f':
        return ('Miss.')
    else:
        return ("Please ender M for male and F for Female")
print(greet(lang),address(gender), name)
'''
'''
a = input('A = ')
b = input('B = ')
def addnum(a, b):
    added = int(a) + int(b)
    return added

x = addnum(a,b)
print(x)
'''
'''
x = 'banana'
y = max(x)
print(y)

def func(x) :
    print(x)

func(10)
func(20)

def stuff():
    print('Hello')
    return
    print('World')

stuff()

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
'''

'''
try:
    hours = float(raw_hours)
    rate = float(raw_rate)
except:
    print("Error! Enter Valid Number")
    quit()
'''
'''
raw_hours = input("Enter Hours:")
raw_rate = input("Enter Rate:")

hours = float(raw_hours)
rate = float(raw_rate)
'''
'''
def computepay(hours, rate):
    if hours<=40:
        return (hours * rate)
    elif hours > 40:
        return ((40 * rate) + ((hours - 40) * (rate * 1.5)))
    else:
        return ("Error")

print(computepay(45, 10.5))
'''
'''
pay = computepay(hours, rate)
print(pay)
'''

