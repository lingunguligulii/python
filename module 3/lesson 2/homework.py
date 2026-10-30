def average_of_three(a, b, c):
    average = (a + b + c) / 3
    return average

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

result = average_of_three(num1, num2, num3)

print("The average is:", result)