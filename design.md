# Save the Watermelon: Design

## Problem Description
Save the Watermelon is a terminal-based word-guessing game. It is intended for anyone who wants to play a simple guessing game and practice letter recognition. The player tries to reveal a secret word before using all available slices.

## Game Rules
1. The game randomly selects a word and hides its letters.
2. The player enters one letter per turn.
3. A valid correct guess reveals every occurrence of that letter and does not use a slice.
4. A valid incorrect guess uses one slice.
5. Inputs that are invalid or have already been guessed are rejected and do not use a slice.
6. The player wins by revealing every letter in the word.
7. The player loses when no slices remain before revealing the word.
8. After a round, the player can choose to play again.

## Program Data
- `secret_word`: the randomly selected word.
- `guessed_letters`: a set of letters already guessed. A set makes repeated guesses easy to detect.
- `slices_remaining`: the number of incorrect guesses still allowed.
- `guess`: the player's current input.

## Program Organization
- `choose_word()`: selects a random word.
- `display_word()`: shows guessed letters and underscores for hidden letters.
- `validate_guess()`: checks that a guess is one unused letter from A to Z.
- `process_guess()`: records a valid guess and updates the slice count.
- `has_won()`: checks whether all letters have been guessed.
- `play_game()`: runs one round.
- `main()`: lets the player replay rounds.

## Program Flow
Start → Select a random word → Initialize guessed letters and slices → Display hidden word → Ask for a guess → Validate input → If invalid, show message and ask again → If valid, record guess → If incorrect, remove one slice → Check win/loss → Repeat while the round continues → Show result → Ask to play again → End or start another round.
