#Save the Watermelon Project

Problem Desc.-
What the program does: A game similar to hangman where a player needs to guess letters to uncover a specific word in a certain amount of rounds
Intended player: Gamers, coders, people who want to pass time
Player goal: Reveal the word by guessing letters before running out of watermelon slices

Game Rules-
How does the game begin: A random word is selected and shown to the player through underscores
What happens when a player makes a guess: When the player inserts a letter, the program will give an output
Correct Guess: The letter will be shown in the unknown word, and the player will not lose any slices
Incorrect Guess: A slice of watermelon will dissapear and the player has fewer chances to guess the word correctly
How to win: Guess all of the letters in the word with remaining watermelon slices
How you lose: Run out of slices because a player guessed incorrectly too many times

Program Data-
How will the program keep track of information:
Secret word: The string containing the random word
Letters already guessed: A set that tracks the letters that have been guessed 
Revealed letters: A set that tracks the letters that have been correctly guessed
Remaining slices: A number that shows the number of incorrect guesses left before losing

Program Organization-
display_word(secret_word,guessed_letters):Outputs a string of revealed letters in the word and hidden letters from the underscores
play_game(): The start point of the game, a loop that retains the game and if it wants to continue to be played or not
select_random_word(): Selects and returns a random word from a list that's been predefined
get_player_guess(Guessed_letters): Asks player to input a letter and gives feedback from response

Program Flow
1. Begin program and verbalize variables nessesary 
2. Select a random word and display it with underscores to keep the word itself hidden
3. Tell player to guess a letter and give input (correct/incorrect)
4. Show player their status after guessing the letter (if there are slices remaining or if a letter appears)
5. Check if player wins or loses based on guesses
6. End or restart program