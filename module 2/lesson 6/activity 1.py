number = 123

temp = number
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp = temp // 10

print(digit_sum)
