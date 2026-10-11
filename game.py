from words import select_random_word
from logic import display_board, is_valid_input, has_won

def play_game():
    print("Save the Watermelon!")
    #Outer replay loop:
    while True:
        #Setting up the game
        secret_word = select_random_word()
        guessed_letters = []
        slices=7

        #Setting up main loop
        while slices > 0:
            print("Word:"+ display_board(secret_word, guessed_letters))
            print("Slices left:" + str(slices))
            print("Guessed letters:" + str(guessed_letters))

            #Player inserts a letter
            guess=input("\n" "Enter your guessed letter: ").lower()

            #Check accuracy
            if is_valid_input(guess, guessed_letters) == False:
              continue

            #Add letter to letters guessed list
            guessed_letters.append(guess)

            #Check if letter is in secret word
            if guess in secret_word:
                print("\n" "Nice! " +guess+ " is in the secret word.")
            else:
                slices= slices-1
                print("\n" "Nice try but " +guess+ " is not in the secret word.")

            if has_won(secret_word, guessed_letters) == True:
                print ("\n" "You won and saved the watermelon!")
                print(display_board(secret_word, guessed_letters) + " was the secret word!")
                return

        #If player loses
        if slices==0:
            print("\n""Game over. You failed to save the watermelon")
            print("The word was:" + secret_word)

        #If player would like to play again
        play_again= input("\n" "Would you like to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing Save the Watermelon!")
            break

#Run the game again
if __name__=="__main__":
    play_game()


