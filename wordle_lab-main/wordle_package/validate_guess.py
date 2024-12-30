"""Module for validating input guess.
    Functions:
    - check_guess_valid: Checks if a guess is a valid 5-letter word.
    - get_valid_guess: Gets a valid guess from the user.
"""

from typing import List


def check_guess_valid(guess: str) -> bool:
    """Check if the guess is a valid 5-letter word
    Return: True if the guess is valid, False otherwise
    """
    if len(guess) == 5 and guess.isalpha() and guess.islower:
        return True
    return False


def get_valid_guess(all_words: List[str], guesses: List[str]) -> str:
    """Get a valid guess from the user
        Must be:
        1. 5 letter word (lower case)
        2. not previously guessed
        3. exists in words.txt
    """
    while True:
        guess = input("enter your guess: ")
        if check_guess_valid(guess) == False:
            print("Guess must be in lower case, with 5 letters and all the letter must be alphabet")
            continue
        elif guess in guesses:
            print("your already test this guess")
            continue
        elif guess not in all_words:
            print("your guess doesn't exist in our dictionnary of words")
            continue
        return guess

def main():
    print(get_valid_guess(['youssef', 'walid','alae'], ['salma']))

if __name__ == "__main__":
    main()

