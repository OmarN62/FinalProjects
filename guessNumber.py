import random
secretNumber = random.randint(1,20)
print("I'm thinking about a number between 1 and 20\nTake a guess")
for guesses in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

    if guess == secretNumber:
        print("Good job! You guessed")
    else: 
        print("Nope. The number I was thinking of was " + str(secretNumber))

 #1.functions can be reused, reduce need for duplicate code  
        #2.when the function is called
        #3.def statement creates a function
        #4.function is the block of code consisting of def 
        #4.function call is when you call the function
        #5. One global scope, a local scope is created when
        # a function is called
        #6.When a function returns the local scope is destroyed & variables too
        #7. A return value is the value that a function call evaluates to   
        #8.If there's no return statement for a function its return value is None
        #9. A global statement will force a variable in a function to refer to the global variable
        #10. Data type of None is None Type
        #11. Import statement imports a module
        #12. The function can be called with spam.bacon()
        #13. Place the line of code that might cause an error in a try clause
        #14. Code that could cause an error goes in the try clause.
        #Code that executes if an error happens goes in the except clause