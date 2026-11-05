import math
print("CIRCLE MEASUREMENT TOOL")
print("========================")

radius = float(input("Enter the radius of the circle: "))

if radius <= 0:
    print("Please enter a positive number.")
else:
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    area = math.pi * radius ** 2

    print("----- RESULTS -----")
    print("Radius:", radius)
    print("diameter:", round(diameter, 2))
    print("Circumference:", round(circumference, 2))
    print("Area:", round(area, 2))

    print("Thank you for using the calculator!")