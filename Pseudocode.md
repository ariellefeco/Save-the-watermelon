#Save the Watermelon-Pseudocode
#Setting up the game and replay loop
WHILE play_again is equal to "yes":
    #Set game variables
    SET word_list= ["english","capitalize","standard","ocean"]
        CHOOSE a random word from word_list and store it as secret_word
        SET slices = 10
        SET guessed_letters=[]
        
        #Main Loop
        WHILE slices>0:
            #Display hidden word
        SET displayed_word=""
        FOR each letter IN secret_word:
            IF letter is IN guessed_letters:
                ADD letter to displayed_word:
            ELSE:
                ADD "_" to displayed_word
        
        PRINT displayed_word
        PRINT "Remaining slices:" + slices
        
        #Guessing
        GET user input and store as guess
        CONVERT guess to lowercase
        
        #Check input
        IF length of guess !=1:
            PRINT "Please enter one letter only."
            CONTINUE the loop

        IF guess is IN guessed_Letters:
            PRINT "You already guessed this letter!"
            CONTINUE the loop
        
        IF guess is other than an English Alphabet letter:
            PRINT "Please enter a valid English letter."
            CONTINUE the loop

        #Add a valid guess to the list
        ADD guess to guessed_letters

        #Check accuracy of guess
        IF guess is IN secret_word:
            PRINT "Nice! That letter is in the word, you are one step closer to winning!"
        ELSE:
            SET slices = slices -1
            PRINT "Nice try, but not exactly right. Bye Bye watermelon slice..."
        
        #Check if game is won
        SET has_won = True
        FOR each letter IN secret_word:
            IF letter NOT IN guessed_letters:
                SET has_won = FALSE
        IF has_won is TRUE:
            PRINT "You saved the watermelon! Congratulations on winning!"
            BREAK out of game loop

    #Check if game is lost
    IF slices==0:
        PRINT "You ran out of slices. GAME OVER."
        PRINT "The word was:" +secret_word

    #Ask to play again
    PROMPT user: "Would you like to play again? Yes/No?
    GET play_again responce

PRINT "Thanks for playing Save the Watermelon!"