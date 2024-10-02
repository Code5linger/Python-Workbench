def calculate_total(exp):
    total = 0
    for item in exp:
        total=total+item
    return total

tom_exp = [2100, 3400, 3500]
joe_exp = [200, 500, 700]

# total = 0

# for item in tom_exp:
#     total=total+item

# print("Tom's totla: ", total)

# total = 0
# for item in joe_exp:
#     total=total+item

# print("Joe's totla: ", total)

tom_total = calculate_total(tom_exp)
joe_total = calculate_total(joe_exp)

print("Tom's totla: ", tom_total)
print("Tom's totla: ", joe_total)

def sum(a,b):
    """
        This 
    """
    total=a+b
    return total

print('Total ', sum(5,7))