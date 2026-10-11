Test plan cases:

1. Correct Guess (Valid Input):
    Enter a single English alphabet letter included in the secret word 
    letter is revealed among the underscores and all the slices are remaining

2. Invalid Input (character other than an English alphabet letter):
    Enters a number or character than isn't a letter
    Rejects this responce and displays a message asking to display an English alphabet letter (a-z)

3. Invalid Input (too many characters guessed at once):
    Enters an entire word instead of one letter
    Displays a message asking to enter a single letter only

4. Incorrect Guess (Valid Input):
    Letter is not in the word
    Lose a watermelon slice

5. Duplicate Input (Already guessed the letter):
    Enters a letter that has been guessed before
    Message stating that letter has been guessed already
    No slices have been lost

6. Winning:
    Deciphered the word without running out of slices
    Reveals final word and congratualtory message

7. Losing:
    Failed to decipher word before running out of slices
    Reveals loss message

8. Replay loop:
    Asks if player would like to continue with a yes/no question
    If player inputs yes, game loops

9. Exit loop:
    Asks if player would like to continue with a yes/no question
    If player inputs no, game ends
    Displays thank you message