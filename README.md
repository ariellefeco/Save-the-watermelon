# Save the Watermelon

## Project Description
Save the Watermelon is a terminal-based Python word-guessing game. The computer chooses a word, and the player guesses one letter at a time to reveal it before using all six slices.

## Game Rules
- Guess one letter per turn.
- Correct guesses reveal every occurrence of the letter.
- Incorrect valid guesses use one slice.
- Invalid or repeated guesses do not use a slice.
- Reveal the entire word to win.
- Run out of slices before revealing the word and you lose.
- Choose whether to play another round after each game.

## Requirements
- Python 3
- A terminal or IDE that can run Python

## Run the Program
From the root folder of the repository, run:

```bash
python src/game.py
```

If your system uses `python3` instead, run:

```bash
python3 src/game.py
```

## Project Structure
- `src/game.py`: runs the game and replay loop.
- `src/logic.py`: contains word display, validation, guess processing, and win-checking functions.
- `src/words.py`: contains the word list and random word selection.
- `docs/design.md`: design document.
- `docs/pseudocode.md`: pseudocode.
- `docs/test-plan.md`: test cases and results.

## Features
- Random word selection
- Hidden word display
- Case-insensitive guesses
- Input validation
- Repeated-guess detection
- Six incorrect guesses allowed
- Win/loss detection
- Replay option

## Known Limitations
- Words are selected from a fixed list in `src/words.py`.
- The game accepts English letters A to Z only.
- Test results must be completed after running the tests.
