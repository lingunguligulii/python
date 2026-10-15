start = int(input("Enter the starting number: "))
end =  int(input("Enter the ending number: "))

for num in range(start, end+1):
    if num < 0:
        continue
    print("Processing: ", num)