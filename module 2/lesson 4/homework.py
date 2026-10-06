size = int(input("Enter the diamond size: "))

for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(size - 1, 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")

    print()
