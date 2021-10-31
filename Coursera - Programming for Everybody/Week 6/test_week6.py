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

lang = input('en es fr: ')
def greet(lang):
    if lang == 'es':
        print('Hola!')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
print(greet(lang))
