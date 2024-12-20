import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generator_problems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expression = str(left) + "" + operator + "" + str(right)
    answer = eval(expression) # here this eval() function is evaluate the expression and give us the the right answer of the expression so that we can check that the user's guess is right or not 
    
    # here we use that because to evaluate the expression we have to use if elif statement and it is time consuming and little harder if there are more number of operators
    return expression, answer


correct = 0
input("Press Enter to start...")
print("---------------------")

start_time = time.time() 
# time starts from here
# here we use the time library to count the time that in how much time user take to complete the quiz

for i in range(TOTAL_PROBLEMS):
    expression, answer = generator_problems()
    
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expression + " = ")
        if guess == str(answer):
            correct +=1
            break
        else: # if user give wrong answer then question is skipped
            break

    
# time ends at here
end_time = time.time()

total_time = round(end_time - start_time, 2)

print("------------------------")

print("Nice work ! You finished the quize in ", total_time, " second\n","               You got ", correct, " correct ans out of ", TOTAL_PROBLEMS)