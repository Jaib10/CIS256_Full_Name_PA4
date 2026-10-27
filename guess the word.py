
# Your Name
# CIS256 Fall 2026
# Programming Assignment 4

import random

# List of words for the game
WORDS = ["apple", "banana", "orange", "grape", "peach"]

# Choose a random word from the list
def choose_word():
    return random.choice(WORDS)

# Check if the guessed letter is in the word
def check_guess(word, letter):
    return letter in word

# Show correct letters and hide missing letters
def display_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()

# Start the word guessing game
def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Guess the Word!")
    print("You have 6 incorrect attempts.")

    # Continue until the player wins or loses
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts remaining:", attempts)

        guess = input("Guess a letter: ").lower().strip()

        # Make sure the player enters one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.")
            continue

        # Prevent repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        # Check whether the guess is correct
        if check_guess(word, guess):
            print("Correct guess!")
        else:
            attempts -= 1
            print("Incorrect guess!")

        # Check whether all letters were guessed
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

    # Message when the player runs out of attempts
    print("\nGame Over!")
    print("The correct word was:", word)


# Run the game when this file is executed
if __name__ == "__main__":
    play_game()
