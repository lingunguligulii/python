end = int(input("Enter the range: "))
count = 0

for number in range (2, end):
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
       
    if is_prime==True:
        count += 1
        print(number)
print("Number of prime numbers: ", count)
