def calculate_bill(units):

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = units * 7
    else:
        bill = units * 10
    
    return bill
units = int(input("Enter electricity units used: "))
bill = calculate_bill(units)
print("Estimate bill:", bill)
    