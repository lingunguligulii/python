score = 0

player_name = input("Enter your name: ")

def add_points():
    global score
    score += 10
    print("You earned 10 points!")

def lose_points():
    global score
    score -= 5
    print("You lost 5 points!")

def bonus():
    global score
    score += 20
    print("You received a 20-point bonus!")

def show_local_score():
    score = 100
    print("Local score:", score)

add_points()
lose_points()
bonus()

show_local_score()

print("\nPlayer:", player_name)
print("Final global score:", score)