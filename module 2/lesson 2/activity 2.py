while True:
    print("---Menu---")
    print("1. Burger - $5")
    print("2. Pizza - $8")
    print("3. salad - $4")

    choice = input("Choose an item (1-3) or 'q' to quit: ")
    if choice == '1':
        print("Your chose Burger. Total: $5")
    elif choice == '2':
        print("Your chose Pizza. Total: $8")
    elif choice == '3':
        print("Your chose salad. Total: $4")
    elif choice.lower() == 'q':
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice. Please try again.")