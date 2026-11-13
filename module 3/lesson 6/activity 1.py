import math

print("--- Math Challenge Lab ---")

number = float(input("Enter a number: "))
print("Square root:", math.sqrt(number))

base = float(input("Enter the base: "))
power = float(input("Enter the power: "))
print("Result:", math.pow(base, power))

dec_number = float(input("Enter a decimal number: "))
print("Rounded up:", math.ceil(dec_number))
print("Rounded down:", math.floor(dec_number))

radius = float(input("Enter radius for circle: "))
circumference = 2 * math.pi * radius
print("circumference:", circumference)