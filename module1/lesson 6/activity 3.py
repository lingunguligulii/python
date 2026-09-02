weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in cm:"))

bmi = weight / (height/100)**2
bmi = round(bmi,2)
print(f"Your BMI is {bmi}")

if bmi <= 18.4:
    print("Category: Underweight")
elif bmi <= 24.9:
    print("Category: Healthy")
elif bmi <= 29.9:
    print("Category: Overweight")
elif bmi <= 34.9:
    print("Category: Severely Overweight")
elif bmi <= 39.9:
     print("Category: Obese")
else:
    print("Category: Severely obese")