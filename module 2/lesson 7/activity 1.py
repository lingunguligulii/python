correct_password = "Python123"

attempts = 5

for attempt in range(1, attempts+1):
    password = input("Enter your password: ")

    if password == correct_password:
        break
    else:
        print("Incorrect Password")

print("Program Finished!")

