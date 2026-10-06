import time
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))

for hour in range(hours):
    for minute in range(minutes):
        print(f"Hour: {hour:02d}:{minute:02d}")
        time.sleep(1)
    print()