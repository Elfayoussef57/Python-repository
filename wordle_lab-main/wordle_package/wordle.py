"""Module for the Wordle game.
Module for the Wordle game.

    Functions:
    - check_guess_correct: Checks if a guess is correct.
    - find_all_char_positions: Finds all positions of a character in a word.
    - feed_back_word: Provides feedback on a guess compared to the word.

    Constants:
    - MAX_ATTEMPTS: The maximum number of attempts allowed in the game.
"""
from typing import List
from colorama import Fore

# Max attempts of the game

MAX_ATTEMPTS = 6



def check_guess_correct(word: str, guess: str) -> bool:
    """Check the guess against the word
    Return: True if the guess is correct, False otherwise
    """
    if guess == word  and MAX_ATTEMPTS >= 0:
        return True
    return False

def contain(character, word):
    test = 0
    for i in range(len(word)):
        if character == word:
            test += 1
    return test
    
def feed_back_word(word: str, guess: str) -> List[str]:
    """Check the guess against the word and return the feedback
    Return: a list with the feedback for each letter in the guess
    """
    count = 0
    feed_back = []
    # Initialize the feedback list
    # It will contain the colors for each letter in the guess
    # The default color is RED for all the letters
    # GREEN for the correct letter in the correct position
    # YELLOW for the correct letter in the wrong position
    for c in word:
        if c == guess[count]:
            feed_back += Fore.GREEN + c + Fore.RESET
            count += 1
        elif c in guess and c != guess[count] and ((c not in feed_back) or contain(c, word) == 2):
                feed_back += Fore.YELLOW + c + Fore.RESET
                count += 1
        else:
            feed_back += Fore.RED + c + Fore.RESET
            count += 1
                
    return feed_back

def main():
    if check_guess_correct("admin", "abled"):
        print("correct!")
    else:
        feed = feed_back_word("admin","abled")
        noun = ''
        for c in feed:
            noun += c
    print(noun)

if __name__ == "__main__":
    main()

