balance = 1000

while True:
    print("--ATM Simulator--")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance: ", balance)
    elif choice == 2:
        amount = int(input("Enter the amount to deposit: "))
        balance = balance + amount
        print("Deposit Successful!")
        print("New Balance: ", balance)
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if balance >= amount:
            balance = balance - amount
            print("Withdraw Successful!")
            print("New Balance: ", balance)
        else:
            print("Insufficient Fund")
    elif choice == 4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid Input, Try again")
