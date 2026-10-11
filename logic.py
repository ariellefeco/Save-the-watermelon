"""Functions that handle the rules of Save the Watermelon."""


def display_word(secret_word, guessed_letters):
    """Return the secret word with unguessed letters hidden."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def validate_guess(guess, guessed_letters):
    """Return (is_valid, message) after checking a player's guess."""
    guess = guess.strip().lower()

    if len(guess) != 1:
        return False, "Enter exactly one letter."
    if not guess.isalpha() or not guess.isascii():
        return False, "Enter one letter from A to Z."
    if guess in guessed_letters:
        return False, "You already guessed that letter."

    return True, guess


def process_guess(guess, secret_word, guessed_letters, slices_remaining):
    """Record a valid guess and return updated slices and a message."""
    guessed_letters.add(guess)

    if guess in secret_word:
        return slices_remaining, f"Correct! The letter '{guess}' is in the word."

    slices_remaining -= 1
    return slices_remaining, f"Incorrect. You lost one slice."


def has_won(secret_word, guessed_letters):
    """Return True when every letter in the secret word has been guessed."""
    return all(letter in guessed_letters for letter in secret_word)
