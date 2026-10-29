def calculate_bill(price, quantity, discount_percent):
    subtotal = price * quantity

    discount = subtotal - discount_percent / 100

    final_total = subtotal - discount

    print("Subtotal:", subtotal, "Taka")
    print("Discount:", discount, "Taka")
    print("Final Total:", final_total, "Taka\n")

print("===== ORDER 1: POSITIONAL ARGUMENTS ======")
calculate_bill(50, 4, 10)

print("===== ORDER 2: KEYWORD ARGUMENTS =====")

calculate_bill(
    quantity=3,
    discount_percent=20,
    price=40
)