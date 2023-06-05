'''
You can run this code and play Rock, Paper, Scissors against the computer. 
The program will prompt you for your choice, display the computer’s choice, and determine the winner based on the rules of the game. 
It will then ask if you want to play again.
'''

import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ")

    while choice.lower() not in ['rock','paper','scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ")
    return choice.lower()

def get_computer_choice():

    choices = ['rock','paper','scissors']
    return random.choice(choices)

def determine_winner(user_choice,computer_choice):

    if user_choice == computer_choice :
        return "It's a tie!"
    elif(
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or 
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You Win!"
    else:
        return "Computer Win"

def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    return choice.lower()

def play_game():
    print("Welocme to Rock, Paper, Scissors!!!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice,computer_choice))
        play_one_more = play_again()
        if play_one_more == "yes":
            continue
        else:
            print("Thank you for playing Rock, Paper, or Scissors!")
            break
        
if __name__ == "__main__":
    play_game()