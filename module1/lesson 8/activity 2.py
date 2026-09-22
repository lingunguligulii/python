bill = float(input("Enter the bill amount:"))

if bill >= 500:
    discount = bill * 0.20
elif bill >= 300:
    discount = bill * 0.10
else:
    discount = 0

final_amount = bill - discount

print(f"Your Bill: {bill}BDT")
print(f"Your Discount: {discount}BDT")
print(f"Your Final Payable Amount: {final_amount}BDT")