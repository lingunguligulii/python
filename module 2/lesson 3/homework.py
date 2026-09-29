total = 0

for r in range(2):
    for c in range(3):
        number = int(input(f"Enter a number for the cell [{r+1}][{c+1}]: "))
        total += number

print("The total is:", total)