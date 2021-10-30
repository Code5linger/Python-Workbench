"""
x_raw = input("Enter a Number: ")
x = int(x_raw)
if x < 2 :
    print('Below 2')
elif x >= 2 :
    print('Two or More')
else :
    print('Big Fish')
"""
"""
x_raw = input("Enter a number: ")
x = int(x_raw)

if x < 2 :
    print("Below 2")
elif x < 20 :
    print("Below 20")
elif x < 10 :
    print("Below 10")
else :
    print("Something Else")
"""
"""
x = "My Name is Jeff"
try:
    i = int(x)
except:
    i = -404
print("Hi", i)
"""
"""
astr = '123x'
try:
    aint = int(astr)
except:
    aint = -304

print("Yo!", aint)
"""
"""
astr = "Bob"
try:
    print("Hello!")
    aint = int(astr)
    print("There")
except:
    aint = -204
print("Done", aint)
"""
"""
rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print('Thanks')
else:
    print("Not a Number", ival)
"""
"""
x =6
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
"""
"""
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')
"""
"""
x = 2.0
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')
"""
raw_hours = input("Enter Hours:")
hours = float(raw_hours)
raw_rate = input("Enter Rate:")
rate = float(raw_rate)

if hours <= 40:
    print(hours * rate)
elif hours > 40:
    print((40 * rate) + ((hours - 40) * (rate * 1.5)))
else:
    print("Error")
