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

