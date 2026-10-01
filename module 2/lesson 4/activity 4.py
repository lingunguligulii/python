rows = int(input("Enter the size of the pattern: "))

for row in range(rows):
    for col in range(rows):
        if row == 0 or row == rows - 1 or col == 0 or col == rows -1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
