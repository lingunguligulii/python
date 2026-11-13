import datetime

day = int(input("Enter your birth day: "))
month = int(input("Enter your birth month: "))

today = datetime.date.today()
birthday = datetime.date(today.year, month, day)

if birthday < today:
    birthday = datetime.date(today.year + 1, month, day)

remaining = birthday - today

if remaining.days == 0:
    print("Happy Birthday!")
else:
    print("Your birthday is in", remaining.days, "days!")

reminder_date = birthday - datetime.timedelta(days=7)
print("Birthday reminder date:", reminder_date)
