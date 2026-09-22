score = 0

q1 = input("Q1: What is the capital of france?")
if q1.lower() == "paris":
    score += 1

q2 = input("Q2: What is 32 times 5?")
if q2.lower() == "160":
    score += 1

q3 = input("Q3: What is are we learning now?")
if q3.lower() == "python":
    score += 1

print(f"Your score is: {score}/3")