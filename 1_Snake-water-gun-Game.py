# import random

# computer = random.choice(["snake", "water", "gun"])
# userInput = input("Enter your choice: ")
# choice = {"snake","water","gun"}

# print(f"\ncomputer choose - {computer} \nuser choose - {userInput}\n")

# if(computer == userInput):
#     print("Match is draw !!!")
# else:
#     if(computer == "snake" and userInput == "water"):
#         print("User lose the game :( \t computer won the game :) ")
#     elif(computer == "snake" and userInput == "gun"):
#         print("User won the game :) \t computer lose the game :) ")
#     elif(computer == "water" and userInput == "snake"):
#         print("User won the game :) \t computer lose the game :) ")
#     elif(computer == "water" and userInput == "gun"):
#         print("User lose the game :) \t computer won the game :) ")
#     elif(computer == "gun" and userInput == "snake"):
#         print("User lose the game :) \t computer won the game :) ")
#     elif(computer == "gun" and userInput == "water"):
#         print("User won the game :) \t computer lose the game :) ")
#     else:
#         print("Something went wrong !!! ")


# -----> imporeved code 

import random

choices = ["snake", "water", "gun"]

def determine_winner(computer, user):
    if(computer == user):
        return "It's a draw !!! "
    
    if((computer == "snake" and user == "gun") or 
    (computer == "water" and user == "snake") or 
    (computer == "gun" and user == "water")):
        return "computer lose and user won the game "
    
    return "computer won and user lose the game "

#main function 
def swg_game():
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (snake, water, gun): ").lower()

    while user_choice not in choices:
        print("Invalid choice ! please re-enter your choice : ")
        input("Enter your choice (snake, water, gun): ").lower()
    
    print(f"\ncomputer choice : {computer_choice} \nuser choice : {user_choice}")

    result = determine_winner(computer_choice, user_choice)
    print(result)

swg_game()