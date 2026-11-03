def calculate_score(points, bonus):
    final_score = points + bonus
    return final_score
    print("Never gets executed")

points = int(input("Enter the points: "))
bonus = int(input("Enter the bonus: "))

total_score = calculate_score(points, bonus)
print("The total score is:", total_score)