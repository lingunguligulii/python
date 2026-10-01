rows = int(input("Enter the number of rows:"))

for row in range(1, rows + 1):
    for col in range(1,rows - row + 1):
        print(" ",end="")

    for col in range(2 * row - 1):
        print("*", end="")

    print()