def calculate_score(correct_answers, bonus, penalty):
    score = correct_answers * 5
    score = score + bonus
    score = score - penalty

    return score

def display_result(student_name, score):
    print("Student:", student_name)
    print("Final score:", score)
    print()

print("===== STUDENT 1 =====")
name1 = input("Enter student name: ")
correct1 = int(input("Enter correct answers: "))
bonus1 = int(input("Enter bonus points: "))
penalty1 = int(input("Enter penalty points: "))
score1 = calculate_score(correct1, bonus1, penalty1)
display_result(name1, score1)