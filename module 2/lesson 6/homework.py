print("Data detective")
print("-----------------")

start = int(input("enter the start number: "))
end = int(input("Enter the end number: "))

even_count = 0 
odd_count = 0
sum_multiples_3_5 = 0
sum_of_digits = 0
even_and_multiple_of_5_count = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if num % 3 == 0 or num % 5 ==0:
    sum_multiples_3_5 += num

temp = abs(num)
while temp > 0:
    digit = temp % 10 
    sum_of_digits += digit
    temp = temp // 10
if num % 2 == 0 and num % 5 == 0:
    even_and_multiple_of_5_count += 1

print("---Results---")
print("even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum of multiples of 3 or 5:", sum_multiples_3_5)
print("Sum of all digits:", sum_of_digits)
print("Even numbers divisible by 5:", even_and_multiple_of_5_count)


