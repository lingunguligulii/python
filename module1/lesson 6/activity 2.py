age = int(input("Enter your age:"))
height = float(input("Enter your height in cm: "))
has_vip_pass = input("Do you have a vip pass? (True/False):").strip() == "True"

ticket_price = 0
is_allowed_in = True

if height < 100 and not has_vip_pass:
    is_allowed_in = False
    print("Sorry! you are not allowed in the park.")

if is_allowed_in:
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 15
    elif 13 <= age <= 17:
        ticket_price = 20
    else:
        ticket_price = 30

    if has_vip_pass:
        ticket_price = ticket_price * 0.5
        print("Vip Pass Applied! You got a 50% discount.")

    print (f"Access Granted! Your final ticket price is ${ticket_price}")