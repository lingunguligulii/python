import random
times = int(input("How many times should we roll? "))
sides = int(input("How many sides on the die? "))

for i in range(times):
    roll = random.randint(1, sides)

    print("Roll:", roll)

    if roll % 2 == 0:
        print("Even")
    else:
        print("odd")