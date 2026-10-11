"""Word bank for Save the Watermelon."""

import random

WORDS = [
    "watermelon",
    "python",
    "computer",
    "science",
    "college",
    "program",
    "keyboard",
    "function",
    "variable",
    "loop",
    "string",
    "garden",
    "library",
    "mountain",
    "sandwich",
]


def choose_word():
    """Return a randomly selected word from the word bank."""
    return random.choice(WORDS)
