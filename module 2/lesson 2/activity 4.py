correct_password = "python123"
password = ""
attempts = 0
max_attempts = 3

while password != correct_password and attempts <= max_attempts:
    password = input("Enter the password: ")
    attempts += 1

    if password != correct_password:
        print("Incorrect password. Try again.")

if password == correct_password:
    print("Access granted!")
else:
    print("Access denied. Maximum attempts reached")

print(f"Number of attempts: {attempts}")