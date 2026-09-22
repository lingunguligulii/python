age = int(input("Enter your age: "))

if age >= 21:
    print(" Eligible for both voting and driving")
elif age >= 18:
    print(" Can vote but not drive yet")
elif age >= 16:
    print(" Can apply for a learner’s license but can’t vote")
else:
    print(" Not eligible yet")



