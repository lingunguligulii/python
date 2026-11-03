def get_result(player_score, opponent_score):
    if player_score > opponent_score:
        return "You win!"
    elif player_score < opponent_score:
        return "You lose!"
    else:
        return "It's a draw!"
    
player_score = int(input("Enter your score:"))
opponent_score = int(input("Enter opponent's score:"))

result = get_result(player_score, opponent_score)

print("Tournament Result:", result)