while True:
    password = input("Creat a password: ")

    has_upper = False
    has_digit = False

    for character in password:
        has_upper = True
    if character.isdigit():
        has_digit = True
    if len(password) < 8:
        print("Password must have at least 8 characters. ")
        continue
    if not has_upper:
        print("Password needs an uppercase letter. ")
        continue
    if not has_digit:
        print("Password needs a number.")
        continue
    print("Password accepted!")
    break

