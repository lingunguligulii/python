word1 = "python"
word2 = "program"

for char1 in word1:
    # print("ch1: ",char1)
    for char2 in word2:
        # print("ch2: ",char2)
        if char1 == char2:
            print(f"Common Character: {char1}")