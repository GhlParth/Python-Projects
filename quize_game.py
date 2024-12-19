name = input("Enter your name: ")
print(f"Hare Krishna {name}.")

start = input(f"Do you want to play {name} ? ")

if start.lower() != "yes":
    quit()

print("Okay ! let's play :) ")

score = 0

que1 = input("How many chapters are in Bhagvad Gita? ")
if que1.lower() == "seven" or 7:
    print("Hari boll ! Correct answer.")
    score += 1
else:
    print("Incorrect answer !!!")

que1 = input("How many shlokas are in Bhagvad Gita? ")
if que1.lower() == "seven hundred" or 700:
    print("Hari boll ! Correct answer.")
    score += 1
else:
    print("Incorrect answer !!!")

que1 = input("Who is the speaker of Bhagvad Gita? ")
if que1.lower() == "krishna":
    print("Hari boll ! Correct answer.")
    score += 1
else:
    print("Incorrect answer !!!")

que1 = input("Who is the main listener of Bhagvad Gita? ")
if que1.lower() == "arjun":
    print("Hari boll ! Correct answer.")
    score += 1
else:
    print("Incorrect answer !!!")

que1 = input("which place Bhagvad Gita was spoke? ")
if que1.lower() == "kurukshetra":
    print("Hari boll ! Correct answer.")
    score += 1
else:
    print("Incorrect answer !!!")


print("Hari Boll ! You got " +str(score)+ " questions right out of 5. ")
