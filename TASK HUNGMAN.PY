"""
TASK 1: Hangman Game
Goal: Text-based Hangman where player guesses a word letter by letter.
Scope: 5 predefined words, max 6 wrong guesses, console only.
Key Concepts: random, while loop, if-else, strings, lists
"""

import random

WORDS = ["python", "hangman", "computer", "keyboard", "function"]
MAX_WRONG = 6


def choose_word():
    return random.choice(WORDS)


def display_progress(word, guessed_letters):
    # Show underscore for unguessed letters, letter if guessed
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_WRONG} wrong guesses allowed.")
    print("=" * 40)

    while wrong_guesses < MAX_WRONG:
        print()
        print("Word:", display_progress(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG}")
        if guessed_letters:
            print("Guessed so far:", ", ".join(guessed_letters))

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print()
            print(f"🎉 You won! The word was '{word}'.")
            return

        guess = input("Guess a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")

    # If loop exits because wrong_guesses == MAX_WRONG
    print()
    print(f"💀 Game over! You ran out of guesses. The word was '{word}'.")


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()