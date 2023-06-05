'''
In this game, a random word is chosen from a list, and the player needs to guess the letters of the word.
The player starts with 6 attempts, and each incorrect guess reduces the number of attempts remaining. 
If the player correctly guesses all the letters of the word, they win. 
If they run out of attempts, they lose.
'''
import random

def hangman():
    words = ['python', 'hangman', 'programming', 'computer', 'game']
    chosen_word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\n")
        for letter in chosen_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        guess = input("\n\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in chosen_word:
            guessed_letters.append(guess)
            if set(chosen_word) == set(guessed_letters):
                print("\nCongratulations! You guessed the word:", chosen_word)
                break
        else:
            attempts -= 1
            print("Incorrect guess! Attempts remaining:", attempts)

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was", chosen_word)

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        hangman()
    else:
        print("\nThank you for playing Hangman!")

if __name__ == "__main__":
    hangman()