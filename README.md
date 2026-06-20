# Task: Hangman Game

## Goal
A simple text-based Hangman game where the player guesses a word one letter at a time.

## Scope
- Uses a small predefined list of 5 words (no external file or API).
- Player is allowed a maximum of 6 incorrect guesses.
- Pure console input/output — no graphics or audio.

## Key Concepts Used
- `random` — to randomly pick a word from the list each game
- `while` loop — to keep the game running until win/loss
- `if-else` — for guess validation and win/loss logic
- Strings — for building the word display (e.g. `_ _ t h o n`)
- Lists — to store the word list and track guessed letters

## How It Works
1. The program randomly selects a word from a list of 5 predefined words.
2. The player guesses one letter at a time.
3. Correct guesses reveal the letter in its position in the word.
4. Incorrect guesses increase a wrong-guess counter (max 6).
5. The game ends when:
   - The player guesses all letters in the word → **Win**
   - The player reaches 6 wrong guesses → **Loss**
6. After each round, the player can choose to play again.

## How to Run
```bash
python3 task1_hangman.py
```

## Sample Gameplay
========================================

Welcome to Hangman!

The word has 6 letters. You have 6 wrong guesses allowed.
Word: _ _ _ _ _ _

Wrong guesses: 0/6

Guess a letter: p

Good guess! 'p' is in the word.
Word: p _ _ _ _ _

Wrong guesses: 0/6

...

🎉 You won! The word was 'python'.

## File Structure
  TASK HUNGMAN.PY
## Possible Future Improvements
- Add ASCII art for the hangman figure as guesses run out
- Allow difficulty levels (longer words, fewer guesses)
- Load word list from an external file
