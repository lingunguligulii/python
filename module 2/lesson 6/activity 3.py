count = 0
total = 0

for number in range(1, 21):
    if number % 4 == 0:
        count += 1
        total += number

print("Count: ", count)
print("total: ", total)