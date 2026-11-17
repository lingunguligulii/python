import calculator_module

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

print("Addition:", calculator_module.add(num1, num2))
print("Subtraction:", calculator_module.subtract(num1, num2))
print("Multiplication:", calculator_module.multiply(num1, num2))
print("Division:", calculator_module.divide(num1, num2))

from calculator_module import add, multiply
print("Direct Add (8+4):", add(8,4))
print("Direct Multiply (8*4):", multiply(8,4))