import sys
import random

def randNum():
    print("I am thinking of a number between 1 and 20.")
    
    trueAnswer = random.randint(1,21)
    for guess in range(1,7):
        print("Take a guess")
        guess = int(input())
        if guess > trueAnswer:
            print("Your guess is too high")
        elif guess < trueAnswer:
            print("Your guess is too low\nKeepgoing!")
        else: 
            break
    if guess == trueAnswer:
            print("Your guess was correct! You guessed it in: " + str(trueAnswer) + "guesses!")
    else: 
         print("Sorry. the number i was thinking of was: " + str(trueAnswer))
randNum()