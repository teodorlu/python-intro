from random import randint
from time import time

questions = 5
score = 0
total_time = 0.0

for q in range(questions):
    x = randint(0,6)
    y = randint(0,6)
    start_time = time()
    res = input(str(x) + " * " + str(y) + " = ")
    end_time = time()
    question_time = end_time - start_time
    total_time = total_time + question_time
    if res == str(x * y):
        print("Correct in " + str(question_time) + " seconds!")
        score = score + 1
    else:
        print("Nope, " + str(x) + " * " + str(y) + " = " + str(x * y))

print("You got " + str(score) + " out of " + str(questions) + " correct!")
print("Your total time was " + str(total_time) + "!")
