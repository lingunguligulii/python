import random

secret = random.randint(1, 10)
attempts = 3

print('welcome to the Number guessisng game!')
print("Guess a number between 1 and 10.")
print("You have 3 attempts.")

while attempts > 0:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("invalid input! Enter a number.")
        continue
    guess = int(guess)

    if guess < 1 or guess > 10:
        print("Choose a number between 1 and 10.")
        continue

    if guess == secret:
        print("Correct! You win!")
        break
    else:
        attempts -= 1
        print("Wrong guess!")

        if attempts > 0:
            print("Attempts remaining:", attempts)

if attempts == 0:
    print("Game over! The number was", secret)

