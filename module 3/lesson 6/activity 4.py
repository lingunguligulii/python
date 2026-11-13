import datetime

year = int(input("Birth year: "))
month = int(input("Birth month: "))
day = int(input("birth day: "))

birth_date = datetime.date(year, month, day)
today = datetime.date.today()

difference = today - birth_date
total_days = difference.days

years = total_days // 365
remaining_days = total_days % 365
months = remaining_days // 30
days = remaining_days % 30

print()
print("today:", today)
print("total days lived:", total_days)
print(
    "Approximate age:",
    years, "years,",
    months, "months,",
    days, "days"
)

in_100_days = today + datetime.timedelta(days=100)
in_1000_days = today + datetime.timedelta(days=1000)

print("Date after 100 days:", in_100_days)
print("Date after 1000 days:", in_1000_days)