import random

def main():
    #genrate a random naumber
    number = random.randint(1,100)
    # initialize variable for user's guess
    guess = 0
    # loop until user guesses the correct number
    while guess != number:
        # ask user for guess
        guess = int(input("Guess the number (between 1 and 100): "))
        # give feedback based on user's guess
        if guess < number:
            print("Too low. Guess again!")
        elif guess > number:
            print("Too High. Guess again!")
        else:
            print(f"Congratulations, you guessed the number {number}")

# A limit to the number of guesses the user can make


if __name__ == "__main__":
    main()