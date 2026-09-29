text = "programming"

for char in text:
    count = 0

    for letter in text:
        if char == letter:
            count += 1 
    print(f"{char} appears {count} times")