"""Terminal version of Save the Watermelon."""

try:
    from .logic import display_word, validate_guess, process_guess, has_won
    from .words import choose_word
except ImportError:
    from logic import display_word, validate_guess, process_guess, has_won


STARTING_SLICES = 6


def play_game():
    """Run one round of Save the Watermelon."""
    secret_word = choose_word()
    guessed_letters = set()
    slices_remaining = STARTING_SLICES

    print("\nWelcome to Save the Watermelon!")
    print("Guess the secret word one letter at a time.")
    print(f"You have {slices_remaining} slices. Invalid guesses do not cost slices.")

    while slices_remaining > 0 and not has_won(secret_word, guessed_letters):
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")
        print("Slices remaining:", slices_remaining)

        guess = input("Enter a letter: ")
        is_valid, result = validate_guess(guess, guessed_letters)

        if not is_valid:
            print(result)
            continue

        slices_remaining, message = process_guess(
            result, secret_word, guessed_letters, slices_remaining
        )
        print(message)

    if has_won(secret_word, guessed_letters):
        print("\nYou saved the watermelon!")
        print("The word was:", secret_word)
    else:
        print("\nThe watermelon ran out of slices.")
        print("The word was:", secret_word)


def main():
    """Run rounds until the player chooses to stop."""
    while True:
        play_game()
        answer = input("\nWould you like to play again? (y/n): ").strip().lower()

        while answer not in ("y", "n"):
            answer = input("Please enter y or n: ").strip().lower()

        if answer == "n":
            print("Thanks for playing Save the Watermelon!")
            break


if __name__ == "__main__":
    main()
