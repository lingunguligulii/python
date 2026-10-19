secret = 7
attempts = 3
print("Welcome to the guessing game!")
print("Guess the secret number from 1 to 10.")
print("You have 3 attempts.")

while attempts > 0:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Invalid input! Enter a number.")
        continue
    guess = int(guess)
    attempts -= 1

    if guess == secret:
        print("Correct! You win!")
        break
    else:
        print("Wrong guess! ")

    if guess < secret:
        pass

    print("Atemmpts remaining:", attempts)
else:
    print("Game over! The secret number was", secret)