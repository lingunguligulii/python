days_of_month = 30
start_day = 1

for I in range(1, start_day):
    print("  ", end="")

for day in range(1, days_of_month + 1):
    print(f"{day:2d}", end=" ")

    if(day + start_day - 1) % 7 == 0:
        print()