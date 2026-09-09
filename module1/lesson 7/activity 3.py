membership_level = input("Enter your membership level (G/S/P): ").upper()
cart_total = float(input("Cart Total: $"))

if membership_level == "G":
    if cart_total > 200:
        discount = 0.25
elif membership_level == "S":
    if cart_total > 150:
        discount = 0.15
else:
    if cart_total > 100:
        discount = 0.1
total = cart_total - cart_total*discount

print(f"Final Total Bill: ${total}")