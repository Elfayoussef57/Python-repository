"""Module for displaying colored text in the terminal for the Wordle game.

    Functions:
        - header: Prints a header in the terminal.
        - game_instructions: Prints the game instructions in the terminal.
        - game_start_display: Prints the starting message for the game.
        - display_word_feedback: Displays the colored feedback for a guess.

    Constants:
        - COLORS: A dictionary containing ANSI color codes for GREEN, YELLOW, RED, and RESET.
"""


from typing import List


def header() -> None:
    """Print a header in the terminal."""
    header = f"""
----------------------------------------------------------------------------------------------------------
                                                WORDLE GAME
----------------------------------------------------------------------------------------------------------
    """
    print(header)


def game_instructions():
    """Print the game instructions in the terminal."""
    instructions = """ 
                                            Welcome to Wordle!
Instructions:
    1. You have six attempts to guess the five-letter word.
    2. Each guess must be a valid five-letter word.
    3. After each guess, the color of the letters will change to show how close your guess was to the word.
        - GREEN:  Correct letter in the correct position.
        - YELLOW: Correct letter in the wrong position.
        - RED:    Incorrect letter.

Good luck!
----------------------------------------------------------------------------------------------------------
    """
    print(instructions)

def display_win(word: str, attempt: int) -> None:
    """Display for winning"""
    print(f"Congratulations! You guessed the word '{word}' in {attempt} attempts.")


def display_lost(word: str) -> None:
    """Display for losing"""
    print(f"Sorry! You ran out of attempts. The word was '{word}'.")