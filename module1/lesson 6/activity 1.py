age = int(input("Enter your age:"))
is_student = input("Are you a student? (yes/no):").lower()

if age < 5:
    price = 0
elif age <= 12 or is_student == "yes":
    price = 8
else:
    price = 12
print(f"Your ticket price is {price}bdt")
