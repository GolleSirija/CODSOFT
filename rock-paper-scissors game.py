#importing "RANDOM" module to randomize the computer's actions in the game.
import random
your_score=0
computer_score=0
print("WELCOME TO THE 'ROCK-PAPER-SCISSORS' GAME")

#to play several times
while True:
#taking user input
    user_choice = input("Enter a choice (rock, paper, scissors): ")
#computer choice
    comp_choice = random.choice(["rock", "paper", "scissors"])
#displaying the actions chosen by computer and the user
    print(f"\nYou chose {user_choice}, computer chose {comp_choice}.\n")
#determining the  rules
    if user_choice == comp_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif  user_choice == "rock":
        if  comp_choice == "scissors":
            print("Rock beats scissors! You win!")
            your_score+=1
            print("your score: ",your_score)
            print("computer score: ",computer_score)
        else:
            print("Paper beats rock! You lose.")
            computer_score+=1
            print("your score: ",your_score)
            print("computer score: ",computer_score)
    elif  user_choice == "paper":
        if  comp_choice == "rock":
            print("Paper  beats rock! You win!")
            your_score+=1
            print("your score: ",your_score)
            print("computer score: ",computer_score)
        else:
            print("Scissors beats paper! You lose.")
            computer_score+=1
            print("your score: ",your_score)
            print("computer score: ",computer_score)
    elif  user_choice == "scissors":
        if  comp_choice == "paper":
            print("Scissors beats paper! You win!")
            your_score+=1
            print("your score: ",your_score)
            print("computer score: ",computer_score)
        else:
            print("Rock  beats scissors! You lose.")
            computer_score+=1
            print("your score: ",your_score)
            print("computer score: ",computer_score)
        #if user wants to play again
    play_again=input("Do you want to play again?(y/n): ")
    if play_again=='n' or play_again=='N':
        #determining the score
        if your_score>computer_score:
            print("final score is: ", your_score)
            print("YOU WON!")
        elif your_score==computer_score:
            print("THE MATCH HAS TIED")
        else:
            print("final score is: ", computer_score)
            print("COMPUTER WON!")
        print("THANK YOU FOR PLAYING THE GAME!!")

        break