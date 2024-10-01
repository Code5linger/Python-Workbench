# num = input("Enter a number: ")

# num=int(num)

# if num%2==0:
#     print('Number given is Even')
# else:
#     print('Number given is Odd')

indian = ['naan', 'daal']
bd = ['biriani', 'panta']

dish=input('Enter a dish name:')

if dish in indian:
    print('Indian')
elif dish in bd:
    print('Bd')
else:
    print('WTF?')