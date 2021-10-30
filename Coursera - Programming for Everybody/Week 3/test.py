"""""
nam = input("Who are you?")
print("Welcome ", nam)
"""""

# Convert elevator floors
#inp = input('Europe floor?')
#x = 1 + 2 * 3 - 8 / 4
# print(x)
"""
x = int(98.6)
print(x)
"""
"""
name = input("Name? ")
print("Hello ", name)
"""
#2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

# This first line is provided for you
"""
hrs = input("Enter Hours:")
float_hrs = float(hrs)
hourly_rate = input("Enter Hourly Rate:")
float_hourly_rate = float(hourly_rate)
print("Pay:", float_hrs * float_hourly_rate)
"""

hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
total_pay = float(hour) * float(rate)
print("Pay: ", total_pay)