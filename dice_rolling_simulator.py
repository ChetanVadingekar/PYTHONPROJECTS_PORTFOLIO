
'''
This program uses the random module in Python to simulate rolling a six-sided die. 
It prompts the user to press Enter to roll the dice and then displays the result. 
It also asks the user if they want to roll again, and the loop continues until the user chooses to stop.
'''
import random

def rolling():
    return random.randint(1,6)

def main():
    print("Welcome to Dice Rolling Simulator!")
    play_again = "yes"

    while play_again.lower() == "yes":
        input("Press Enter to roll the dice...")
        result = rolling()
        print(f"You rolled a {result}")
        play_again = input("Would you like to roll again? (yes/no): ")
        print("Thank you for playing!")


if __name__ == "__main__":
    main()