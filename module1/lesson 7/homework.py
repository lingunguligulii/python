gpa = float(input("Enter your GPA (0.0 - 4.0): "))
math_score = int(input("Enter your Math score (0 - 100): "))
leadership = input("Do you have leadership experience? (Y/N): ")

# Check GPA requirement
if gpa >= 3.0:
    # Check Math score requirement
    if math_score >= 85:
        print(" STEM path eligible.")

        # Check leadership bonus
        if leadership.upper() == "Y":
            print("+5 scholarship points.")
    else:
        print("Math score too low.")
else:
    print("GPA below threshold.")