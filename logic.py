def display_board(secret_word, guessed_letters):
    #Shows secret word with underscores
    display_output=""
    for letter in secret_word:
        if letter in guessed_letters:
            display_output+= letter
        else:
            display_output+= "_"
    return display_output

def is_valid_input(guess, guessed_letters):
    #States that letter has not been guessed yet
    #Ensures that only one letter is guessed at a time
    if len(guess) != 1:
        print("Please enter a single letter")
        return False

    #Ensures letter is an English alphabet character
    if not guess.isalpha():
        print("Please enter an English letter (a-z)")
        return False

    #Ensures letter has not been guessed yet
    if guess in guessed_letters:
        print("You already guessed this letter")
        return False

    return True

def has_won(secret_word, guessed_letters):
    #Ensures all letters have been guessed in secret word
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True
