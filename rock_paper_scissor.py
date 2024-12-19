import random

print("Hare krishna !!! Let's play a game. ")

option = ["rock", "paper", "scissor"]

computer_win = 0
user_win = 0

while True:
    print(" 1. Rock\n 2. paper\n 3. Scissor\n 4. Quit")
    user_input = int(input("Enter your choice: "))
    
    
    if user_input not in [1,2,3,4]:
        print("Choose valid option.")
        continue
    
    if user_input == 4:
        break
    
    user_choice = option[user_input - 1]
    
    computer_choice = random.choice(option)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    
    if user_choice == computer_choice:
        print("It's Tie !!!")
        
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("You Won!!!")
        user_win += 1
    
    else:
        print("Computer Won !!!")
        computer_win += 1
        
print("You won ", str(user_win) + " times.")
print("Computer won ", str(computer_win) + " times.")