# User      Discord: Bwomp-Womp#2368
#           Git:     GraphicDesignDropout
#           Twitter: @iamtsofu

# Title:    WOP_BeginnerChallenges_02_RockPaperScissors

from random import randint

def unfair():
    quit = False
    while not quit:
        #Resets user choice
        userChoice = input("Rock, Paper, Scissors, quit (r p s q) > ")
        print()
        
        # Compare user choices, bot always wins
        if userChoice in "rpsq":
            if userChoice == "r":
                botChoice = "paper"
                print(botChoice, "\nAha, I win!")
            elif userChoice == "s":
                botChoice ="rock"
                print(botChoice, "\nAha, I win!")
            # I know this is placed weird, I wrote the else first.
            elif userChoice == "q":
                quit = True
            else:
                botChoice = "scissors"
                print(botChoice, "\nAha, I win!")
        else:
            print("Error - please type r, p, or s")

    # Once user quits
    print("Hang on, you're not really leaving are you?")
    print("Okay, look, maybe I wasn't playing totally fair.")
    fair()

def fair():
    quit = False
    while not quit:
        userChoice = input("Rock, Paper, Scissors, quit (r p s q) > ")
        botChoiceGen = randint(0,2)
        print()
        
        if botChoiceGen == 0:
            botChoice = "Rock"
        elif botChoiceGen == 1:
            botChoice = "Paper"
        else:
            botChoice = "Scissors"

        # Plays game again, this time fair
        if userChoice in ("rpsq"):
        
            if userChoice == "q":
                quit = True

            # if rock
            elif userChoice == "r":
                if botChoice == "Rock":
                    print(botChoice, "\nTie!")
                elif botChoice == "Scissors":
                    print(botChoice, "\nUgh, you win...")
                else:
                    print(botChoice, "\nI STILL win.")
                
            # if paper
            elif userChoice == "p":
                if botChoice == "Paper":
                    print(botChoice, "\nTie!")
                elif botChoice == "Rock":
                    print(botChoice, "\nUgh, you win...")
                else:
                    print(botChoice, "\nI STILL win.")

            # if scissors
            else:
                if botChoice == "Scissors":
                    print(botChoice, "\nTie!")
                elif botChoice == "Paper":
                    print(botChoice, "\nUgh, you win...")
                else:
                    print(botChoice, "\nI STILL win.")
        else:
            print("Error - please type r, p, or s")

unfair()
