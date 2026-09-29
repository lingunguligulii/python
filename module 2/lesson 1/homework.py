pin = "1234"
attempts = 3

while attempts > 0:
    user_pin = input("Enter your 4-digit PIN: ")

    if user_pin == pin:
        print("Welcome to your account")
        break
    else:
        attempts -= 1
        print ("Incorrect PIN")
        print("Remaining attempts:", attempts)

if attempts == 0:
    print("Access Denied. Your account has been locked. Please try again later.")