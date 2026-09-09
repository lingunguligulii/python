medical_cause = input("Do you have any medical cause? (yes/no):")

if medical_cause == "no":
    attendance = int(input("Enter you attendance: "))
    if attendance >= 75:
        print("You can sit for the exam")
    else:
        print("You are not eligible for the exam. ")
else:
    print("You can sit for the exam. ")