score = int(input("Enter the student's exam score: "))
previous_score = int(input("Enter the student's previous score: "))
attendance = int(input("Enter attendance percentage: "))


if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)


if score - previous_score >= 40:
    print(" Possible cheating detected: unusually large score increase.")
elif score > previous_score:
    print("Good improvement!")


if attendance == 100:
    print("Perfect attendance! +5 bonus points.")


if score >= 90 and attendance == 100:
    print("Excellent performance and perfect attendance!")
elif score >= 80 and attendance >= 90:
    print("Great job! Keep up the good work.")
elif score >= 50 or attendance >= 75:
    print("You passed. Keep working to improve.")
else:
    print("You need to improve your performance and attendance.")