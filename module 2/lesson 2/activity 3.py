battery = 20

while battery < 100:
    print("Battery level:", battery, "%" )
    battery += 10

print("Battery is fully charged!")

savings = 0
target = 100
week = 1

while savings < target:
    savings += 10
    print(f"Week {week}: Savings = ${savings}")
    week += 1

print ("target savings reached!")