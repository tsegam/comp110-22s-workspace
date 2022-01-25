"""An example of conditional (if-else) statements."""
from random import randint
ANSWER = randint(1, 10)

print("I have a number in mind from 1-10.")

guess: int = int(input("What is it?"))

if guess == ANSWER:
    print("You guessed correct!")
else: 
    print("WRONG. You guessed incorretly :(")
    if ANSWER < guess:
        print("You guessed too high!")
    else:
        print("You guessed too low!")
print("Game over.")