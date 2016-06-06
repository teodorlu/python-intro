from random import randint

questions = 5
score = 0

for q in range(questions):
    x = randint(0,6)
    y = randint(0,6)
    res = input(str(x) + " * " + str(y) + " = ")
    if res == str(x * y):
        print("Correct!")
        score = score + 1
    else:
        print("Nope, " + str(x) + " * " + str(y) + " = " + str(x * y))

print("You got " + str(score) + " out of " + str(questions) + " correct!")
