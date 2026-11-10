import random 

print("Mystery Spinner")
option1 = input("Enter option 1: ")
option2 = input("Enter option 2: ")
option3 = input("Enter option 3: ")
option4 = input("Enter option 4: ")
options = [option1, option2, option3, option4]

while True:
    result = random.choice(options)
    print("The spinner chose:", result)

    again = input("Do you want to spin again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for spinning")
        break