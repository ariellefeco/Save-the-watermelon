Project description.
This is a word guessing game in Python where a player must guess the secret word in the alloted guesses in order to win.
There are three modules in this game called: 
words.py which organizes data,
logic.py which displays the rules and determines whether an input is correct or not, 
game.py which is the game the player will get to partake in

Game rules.
The player must guess a secret word with a limited amount of guesses in order to save the watermelon slices
Each round, the player inputs a letter and the program outputs if it was correct or not
If the player guesses the word before running out of slices, they win
If not, the player loses

Instructions for running the program.
Open the project in PyCharm, find the code directory on the left side. Run the script using python.

Features implemented.
Ensures that inputs are single English alphabet letters and not numbers
Prevents players from guessing the same letter and losing slices
Includes a loop that players can choose to play again without having to restart the game
Able to differentiate capitalized and lowercase letters by using the .lower() input

Known issues or limitations, if any.
The game does not have any graphics, so you must imagine losing watermelon slices
The words are used from a predetermined list and not actually random.
