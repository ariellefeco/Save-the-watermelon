# Save the Watermelon: Pseudocode

## Choose a Word
1. Store a collection of possible words.
2. Randomly select one word.
3. Return the selected word.

## Display the Word
1. For each letter in the secret word:
   - If the letter has been guessed, display the letter.
   - Otherwise, display an underscore.
2. Put spaces between displayed characters.

## Validate a Guess
1. Remove spaces around the player's input and convert it to lowercase.
2. If the input is not exactly one character, reject it.
3. If the character is not an English letter from A to Z, reject it.
4. If the letter has already been guessed, reject it.
5. Otherwise, accept the guess.

## Process a Guess
1. Add the accepted letter to the collection of guessed letters.
2. If the letter appears in the secret word, keep the slice count the same.
3. Otherwise, subtract one from the remaining slices.
4. Report whether the guess was correct.

## Run One Round
1. Select a random word.
2. Start with an empty set of guessed letters and six slices.
3. While slices remain and the player has not won:
   - Display the current word, guessed letters, and slices.
   - Ask the player for a letter.
   - Validate the input.
   - If invalid, display the reason and return to the next turn without changing slices.
   - If valid, process the guess.
4. If every letter has been revealed, display a win message.
5. Otherwise, display a loss message.
6. Reveal the secret word.

## Replay
1. Run one round.
2. Ask whether the player wants another round.
3. If the answer is not y or n, ask again.
4. If the answer is y, start another round.
5. If the answer is n, end the program.
