# num = input("Enter a number: ")
# print(type(num)) # <class 'str'>

# print('You have entered:', num) 

# num=int(num) # <class 'int'>

# print(type(num))

# if num%2==0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

bang = ['panta', 'fish', 'daal']
chinese = ['egg role', 'momo', 'bat']
italian = ['🤌🤌', 'pasta', 'pizza']

dish = input("Enter a dish name:")

if dish in bang:
    print('Bangladeshi')
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print('Italian')
else:
    print('🤌 🤌')