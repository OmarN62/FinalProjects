import random 

print("Welcome to the randomNumber game\nHere we'll be creating a randomNumberGenerating Game.\nPlease enter your name here below")
name = input()

number_toguess = random.randrange(100)

chances = 7

counter = 0 

while counter > chances: 
    counter += 1
    guess = int(input('Enter your guess: '))

    if guess == number_toguess:
        print(f'The number is{number_toguess} you got it !! in the {guess} attempt')
        break

    elif counter >= chances and guess != number_toguess:
        print(f'Sorry about that, The number is {number_toguess} good luck next time')

    elif counter >= chances and guess != number_toguess:
        print(f'Sorry, the number is {number_toguess} good luck next time')
    
    elif guess > number_toguess:
        print('Your guess is higher than the actual')

    elif guess < number_toguess:
        print('Your guess is lower than the actual')