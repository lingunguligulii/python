import random

name = input("Enter your name: ")

print("\nEnter three possible adventure locations:")

locations = []

for i in range(3):
    location = input(f"location {i + 1}:")
    locations.append(location)

characters = [
    "a mysterious wizard",
    "a brave knight",
    "a lost explorer",
    "a talking dragon",
    "a secret agent"
]

challenges = [
    "fight a dangerous monster",
    "solve an ancient puzzle",
    "escape a haunted forest",
    "find a hidden treasure",
    "survive a deadly trap"
]  

rewards = [
    "a magical sword",
    "a bag of gold",
    "an ancient treasure map",
    "a powerful magic potion",
    "a legendary shield"
]

while True:
    random_location = random.choice(locations)
    random_character = random.choice(characters)
    random_challenge = random.choice(challenges)
    random_reward = random.choice(rewards)
    
    print("\n===== YOUR ADVENTURE =====")
    print(f"Welcome, {name}!")
    print(f"You travel to {random_location}.")
    print(f"You meet {random_character}.")
    print(f"Together, you must {random_challenge}.")
    print(f"After succeeding, you receive {random_reward}!")
    print("==========================")

    again = input("\nDo you want another adventure? (yes/no): ").lower()

    if again == "no":
        print(f"\nThanks for playing, {name}!")
        break

    elif again == "yes":
        print("\nGenerating another adventure...")

    else:
        print("Invalid choice! Generating another adventure...")

