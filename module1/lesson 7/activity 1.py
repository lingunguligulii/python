drink = input("Coffee or tea? ").lower()

if drink == "coffee":
    size = input("Size (S/M/L):").upper()
    if size =="S":
        print(f"You ordered {size} size of {drink}. Your total is 80 BDT")
    elif size == "M":
        print(f"You ordered {size} size of {drink}. Your total is 120 BDT")
    else:
        print(f"You ordered {size} size of {drink}. Your total is 200 BDT")

elif drink == "tea":
    sugar_level = int(input("Enter your sugar level (0-2): "))
    if sugar_level == 0:
        print(f"Your ordered {sugar_level} sugar level of {drink}. Your total is 50 BDT")
    elif sugar_level == 1:
         print(f"Your ordered {sugar_level} sugar level of {drink}. Your total is 80 BDT")
    else:
         print(f"Your ordered {sugar_level} sugar level of {drink}. Your total is 120 BDT")

else:
    print("invalid input. Please choose between coffee or tea")