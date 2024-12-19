import random

print("Hi welcome to the game, This is number guessing game. \n You got the seven chances to guess the number. Lets start the game.\n")

number_to_guess = random.randrange(100)

chances = 7 

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    try:
        my_guess = int(input("Please enter your guess: "))
    except: 
        print("Invalid input !! please enter a valid integer. ")
        guess_counter -= 1
        continue

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt.")
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops !! sorry the number is {number_to_guess} better luck next time.")

    elif my_guess > number_to_guess:
        print("Your guess is higher !!")
    
    elif my_guess < number_to_guess:
        print("Your guess is lesser !!")