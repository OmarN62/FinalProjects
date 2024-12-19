import random, sys
print("This is my rock paper scissors game")
wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit()
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("Choose r for rock p for paper or s for scissors or q for quit")
    if playerMove == "r":
        print(playerMove + "\nRock versus...")
    elif playerMove == "p":
        print(playerMove + "\nPaper versus...")
    elif playerMove == "s":
        print(playerMove + "\nScissors versus...")
        
    randNum = random.randint(1,3)     
    if randNum == "1":
        computerMove = "r"
        print("ROCK")
    elif randNum == "2":
        computerMove = "s"
        print("SCISSORS")
    elif randNum == "3":
        computerMove = "p"
        print("PAPER")

    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        losses = losses + 1
        