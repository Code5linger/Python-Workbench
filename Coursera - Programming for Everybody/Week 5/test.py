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

x = "My Name is Jeff"
try:
    i = int(x)
except:
    i = -404
print("Hi", i)

astr = '123x'
try:
    aint = int(astr)
except:
    aint = -304

print("Yo!", aint)