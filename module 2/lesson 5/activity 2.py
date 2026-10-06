size = int(input("Enter the size of the pattern"))

for row in range(size):
    for col in range(size):
        if (row + col) % 2 == 0:
            print("X", end=" ")
        else:
            print("0", end=" ")
    print()