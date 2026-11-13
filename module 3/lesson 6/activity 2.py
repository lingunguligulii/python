import random
import math

secret = random.randint(1, 15)
square = secret ** 2

print("Find the aquare root of:", square)

guess = int(input("Your guess: "))
correct_answer = math.sqrt(square)

if guess == correct_answer:
    print("Correct!")
else:
    print("Wrong!")
    print("The correct answer is:", int(correct_answer))