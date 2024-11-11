import random , sys # importing random / sys module
# defining my function rps for rock paper scissors
def rps():
    #printing out wins / losses / ties varirables
    print("ROCK, PAPER, SCISSORS")
    wins = 0
    losses = 0
    ties = 0
    
    #starts the game, while loop for while True execute the game 
    while True: 
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True:
            print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            #playerMove = input, if input is q, exit, if r p or s, break and enter third if block
            playerMove = input()
            if playerMove == 'q':
                sys.exit() #quitting the program
            if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
                break 
            print('Type r for rock, p for paper, s for scissors, or q for quit')
              
        if playerMove == 'r':
            print('ROCK versus...')
        elif playerMove == 'p':
            print('PAPER versus...')
        elif playerMove == 's':
            print('SCISSORS versus...')

        randomNumber = random.randint(1,3)
        if randomNumber == 1:
            computersmove = 'r'
            print('ROCK')
        elif randomNumber == 2:
            computersmove = 'p'
            print('PAPER')
        elif randomNumber == 3:
            computersmove = 's'
            print('SCISSORS')

        if playerMove == computersmove:
            print("Draw! Its a tie!")
            ties = ties + 1
        elif playerMove == 'r' and computersmove == 's':
            print("You win!")
            wins = wins + 1
rps()