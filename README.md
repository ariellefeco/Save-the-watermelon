Project description.
This is a word guessing game in Python where a player must guess the secret word in the allotted guesses in order to win.
There are three modules in this game called: 
words.py, which organizes data,
logic.py, which displays the rules and determines whether an input is correct or not, 
game.py, which is the game the player will get to partake in

Game rules.
The player must guess a secret word with a limited number of guesses to save the watermelon slices
Each round, the player inputs a letter, and the program outputs whether it was correct or not
If the player guesses the word before running out of slices, they win
If not, the player loses

Instructions for running the program.
Use this command in the project directory  to run the program
'''bash
python src/game.py

Features implemented.
Ensures that inputs are single English alphabet letters and not numbers
Prevents players from guessing the same letter and losing slices
Includes a loop that players can choose to play again without having to restart the game
Able to differentiate capitalized and lowercase letters by using the .lower() input

Known issues or limitations, if any.
The game does not have any graphics, so you must imagine losing watermelon slices
The words are used from a predetermined list and are not actually random.
