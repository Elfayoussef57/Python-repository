"""Module for the Wordle game.
Module for the Wordle game.

    Functions:
    - check_guess_correct: Checks if a guess is correct.
    - find_all_char_positions: Finds all positions of a character in a word.
    - feed_back_word: Provides feedback on a guess compared to the word.

    Constants:
    - MAX_ATTEMPTS: The maximum number of attempts allowed in the game
"""
from typing import List
#we can import the colorama library if we dont know the color code

# Max attempts of the game

MAX_ATTEMPTS = 6



def check_guess_correct(word: str, guess: str) -> bool:
    """Check the guess against the word
    Return: True if the guess is correct, False otherwise
    """
    if guess == word  and MAX_ATTEMPTS >= 0:
        return True
    return False
    
def feed_back_word(word: str, guess: str) -> List[str]:
    """Check the guess against the word and return the feedback
    Return: a list with the feedback for each letter in the guess
    """
    feedback = []
    word_list = list(word)
    
    for i in range(len(guess)):
        if guess[i] == word[i]:
            #green
            feedback.append('\033[92m' + guess[i] + '\033[0m')
            word_list[i] = None  # Mark as used
        else:
            feedback.append(None)

    for i in range(len(guess)):
        if feedback[i] is None:
            if guess[i] in word_list:
                #yellow
                feedback[i] = '\033[93m' + guess[i] + '\033[0m' 
                word_list[word_list.index(guess[i])] = None
            else:
                #red
                feedback[i] = '\033[91m' + guess[i] + '\033[0m'

    return feedback

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


