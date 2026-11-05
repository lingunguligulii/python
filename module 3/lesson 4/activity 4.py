score = 0

def add_points(points):
    global score

    score += points

    print("Points added:", points)
    print("Current score:", score)

def lose_points(points):
    global score

    score -= points

    print("Points lost:", points)
    print("Current score:", score)

earned = int(input("How many points did you earn? "))
lost = int(input("How many points did you lose? "))

add_points(earned)
lose_points(lost)

print("Final score:", score)




