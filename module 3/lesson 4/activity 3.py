player_name = "Alex"
score = 100

def practice_mode():
    score = 50
    print("Practice Score:", score)

def bonus_mode():
    score = 200
    print("Bonus Score:", score)

def challenge_mode():
    score = 75
    score = score * 25
    print("Challenge Score:", score)

print("Player", player_name)
print("Global Score:", score)

print("\n--- Game Modes ---")
practice_mode()
bonus_mode()
challenge_mode()

print("\n--- Final Result ---")
print("Global Score", score)