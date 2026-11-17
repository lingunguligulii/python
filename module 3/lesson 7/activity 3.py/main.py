import grade_module

marks = float(input("Enter your marks: "))
grade = grade_module.calculate_grade(marks)
result = grade_module.check_pass(marks)

print("Marks:", marks)
print("Grade:", grade)
print("Result:", result)
