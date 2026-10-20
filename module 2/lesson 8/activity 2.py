total = 0
item_count = 0

print("Enter item prices.")
print("Type 'done' when finished")

while True:
    entry = input("Enter price: ")

    if entry.lower() == "done":
        break
    price = float(entry)
    total += price
    item_count += 1
if item_count >= 5:
    discount = total * 0.10
    total -= discount
    print("10% discount applied!")

print("---BILL---")
print("Items:", item_count)
print("Total:", total)