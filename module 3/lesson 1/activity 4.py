def calculate_total(price, quantity):
    return price * quantity

def calculate_discount(total, percent):
    return total * percent / 100

price = float(input("Enter item prices: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount percentage: "))

total = calculate_total(price, quantity)

discount = calculate_discount(total, discount_percent)

final_price = total - discount 
print("\n--- SHOPPING SUMMARY ---")
print("Original total:", total)
print("Discount:", discount)
print("Final price:", final_price)