items = int(input("How many items are you buying? "))

total = 0

for i in range(items):
    price = float(input("Enter the price of the item: "))
    total += price

if total > 50:
    total = total * 0.9

print(f"Final amount due: ${total:.2f}")