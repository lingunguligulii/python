rows = int(input("Enter the number of rows: "))
seats = int(input("Enter the number of seats: "))

for row in range (1, rows + 1):
    for seat in range(1, seats + 1):
        print(f"R{row}-S{seat}", end=" ")
    print()