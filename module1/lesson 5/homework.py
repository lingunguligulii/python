temperature = int(input("Enter the temperature in celsius"))

if temperature < 10:
    print("Wear a jacket, trousers and warm shoes. ")
elif temperature < 20:
    print("Wear a sweater and trousers. ")
elif temperature < 30:
    print("Wear a t-shirt and jeans. ")
else:
    print("Wear a t-shirt, shorts, and sandals.")