
# Guess number 
import random 
target = random.randint(1,100)
guess = 0 
while guess != target:
    guess = int(input("Guess a number between 1 and 100 : "))

    if guess < target:
        print("TOO LOW !") 
    elif guess > target:
        print("TOO HIGH!")

print("Correct! You guessed the number. ")
