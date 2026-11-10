import random 

target = random.randint(1, 20)
print("Guess the number (1-20). You have 3 tries.")

for attempt in range(3):
    guess = int(input(f"Guess {attempt + 1}: "))

    if target < guess:
        print("Too high!")
    elif target > guess:
        print("Too low!")
    elif guess == target:
        print("You got it!")
        break

else:
    print("Out of guesses! The number was:", target)