def add_numbers(a, b):
    result = a + b
    print("Sum:", result)

def multiply_numbers(a, b):
    result = a * b
    print("product:", result)

add_numbers(5, 3)
add_numbers(10, 20)
multiply_numbers(4, 6)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add_numbers(num1, num2)
multiply_numbers(num1, num2)
