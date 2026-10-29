def calculate_total(price, quantity):
    total = price * quantity
    return total

def calculate_item_cost(item_name, price, quantity):
    total= calculate_total(price, quantity)

    print(f"Item: {item_name}")
    print(f"price: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total cost: ${total:.2f}\n")

    return total

order1 = calculate_item_cost("apples", 0.5, 10)
order2 = calculate_item_cost("bananas", 0.3, 5)

grand_total = order1 + order2
print(f"Grand total: ${grand_total:.2f}")