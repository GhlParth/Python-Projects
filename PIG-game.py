import random

def roll():
    min_value = 1
    max_value = 6
    
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("Enter the number of players (2 - 4) : ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 to 4 players...")
    else: 
        print("Invalid input. Please try again...")
        
# print(players)

max_score = 50

players_scores = [0 for i in range(players)]
# here we don't know that how many players we get in input so we created the list to store the score of the players and in list we use for loop which initialize the whole list by zero in starting and its length is the number of players are going to play 

# print(players_scores)

while max(players_scores) < max_score:
    
    for player_idx in range(players):
        print("\n Player ", player_idx + 1, " turn has just started... \n")
        print("\n Your total score is: ", players_scores[player_idx], " \n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y) ? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            
            if value == 1:
                print("You got 1, your turn is done.")
                break
            else:
                current_score += value
                print("Your got ", value, " on dice.")
                    
            print("Your score is: ", current_score)
            
        players_scores[player_idx] += current_score
        print("Your total score is: ", players_scores[player_idx])

max_score = max(players_scores)
winnig_idx = players_scores.index(max_score)

print("\n Player ", winnig_idx, " has won the game with a score of ", max_score)