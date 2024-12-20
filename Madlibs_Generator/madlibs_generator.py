with open ("story.txt", "r") as f:
    story = f.read()
    
words = set()
# here we create the set so that we can store only the unique value
start_word = -1

# to get the word which start is enclosed between <> bracket 
target_start = "<"
target_end = ">"

# iterate the loop to full story 
# here this loop works as it takes the index and characters both like if story = "hello" then this loop iterates as (0, h), (1, e).....(4, o)
# it is more readable and efficient and low risk of error
for i, char in enumerate(story):
    if char == target_start: 
        start_word = i
    if char == target_end and start_word != -1:
        word = story[start_word: i + 1] # here it take the slice of that word which starts from the start_word index to the end of index 
        words.add(word) # add the word to the words set
        start_word = -1 # again initialize with zero so that we go for new words to store

# print(words)

answers = {} # here we create a collection because collection has property of something like key: value pair

# answer = {"name" : "Raghav", "age": 15, "gender" : "male"}    like this

for word in words: # iterates to the words which are we stored in the words set
    answer = input("Enter a word for " + word + " : ")
    answers[word] = answer # here we store the answer to the answers collection respectively to the key value pair
    
# print(answers)

for word in words:  
    story = story.replace(word, answers[word]) # now replace the word to the story
    
print(story)