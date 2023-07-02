import random

def play():
    # assigning part for choices and scores
    choices = ['rock', 'paper', 'scissors']
    user = 0
    computer = 0
    draws = 0

    #while loop to continuousely run the app
    while True:
        print("Welcome to the legendary childhood game: Rock, Paper, Scissors!")
        print("Enter 'q' to exit the game.")
        choice = input("Enter your choice (rock, paper, scissor): ").lower()
        computer_choice = random.choice(choices) #inbuilt random funciton 

        if choice == 'q': #if choice q , exit the game
            break

        print("Your choice:", choice)
        print("Computer's choice:", computer_choice)

        if choice not in choices:
             print("Invalid choice. Please try again.") #invalid , go to the next iteration using continue
             continue
        
        if choice == computer_choice:
            print("It's a draw!")
            draws += 1
        elif (
            #logic for wiinings
            (choice == 'rock' and computer_choice == 'scissors') or
            (choice == 'scissors' and computer_choice == 'paper') or
            (choice == 'paper' and computer_choice == 'rock')
        ):
            print("Congratulations! You win!")
            user += 1
        else:
            print("Computer wins!")
            computer += 1

        print("Score: You:", user, "Computer:", computer, "Draws:", draws)
        print()
    
play()