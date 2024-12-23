import random
from collections import Counter

somewords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

somewords = somewords.split(" ")
word = random.choice(somewords)

if __name__ == '__main__':
    print("\n\tGuess the word! \n\t\t HINT: Word is a name of fruit. ")
    
    for i in word:
        print('_', end=' ')
    print()
    
    playing = True
    letterGuessed = ""
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
            
            try:
                guess = input("Enter a letter to guess: ")
            except:
                print("Enter only a letter...")
                continue
            
            
            if not guess.isalpha():
                print("Enter Only a LETTER....")
                continue
            elif len(guess) > 1:
                print("Enter only a SINGLE letter....")
                continue
            elif guess in letterGuessed:
                print("You have already guessed that letter....")
                continue
            
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
    
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=" ")
                    correct +=1
                    
                elif Counter(letterGuessed) == Counter(word):
                    print("The word is: ", end=" ")
                    print(word)
                    flag = 1
                    print("Comgratulation you WON !!!")
                    break
                    break
                else:
                    print("_", end="")
                    
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print("You lost ! Try again... ")
            print(f"The word wad {word}")
        
    except KeyboardInterrupt:
        print()
        print("Bye ! Try Again...")
        exit()
                    