def ticket_cost(price, tickets):
    total = price * tickets
    return total

price = float(input("enter ticket price: "))
tickets = int(input("How many tickets? "))

total = ticket_cost(price, tickets)

print("total ticket cost:", total)

service_fee = total * 0.05

print("Service fee:", service_fee)
print("Final cost:", total + service_fee)
