"""
    This is a python implementation of the Wordle Game.

    Based on the online word game created and developed by Welsh software
    engineer Josh Wardle. Players have six attempts to guess a five-letter word,
    with feedback given for each guess in the form of coloured tiles indicating
    when letters match or occupy the correct position.

    The current version of this project is for education purposes.

    ENSAT 2024/2025.
"""

from wordle_package.wordle import check_guess_correct, feed_back_word
from wordle_package.display import header, game_instructions, display_lost, display_win
from wordle_package.word_choice import read_words_file, choose_random_word
from wordle_package.validate_guess import get_valid_guess
import sys

def main():
    attempts = 6
    test = False
    guesses = []
    feed = ''
    all_words = read_words_file()
    word = choose_random_word(all_words)
    print(word)
    while attempts > 0:
        guess = get_valid_guess(all_words, guesses)
        guesses.append(guess)  # Add the guess to the list of guesses

        if check_guess_correct(word, guess):
            display_win(word, attempts)
            print("Do you want to play again? (yes/no)")
            if input().lower().strip() == "yes":
                main()
            else:
                test = True
                break
        else:
            attempts -= 1
            feedback = feed_back_word(guess, word)
            for c in feedback:
                feed += c
            print(feed)
            feed = ''

    if attempts <= 0 and test == False:
        display_lost(word)
        print("Do you want to play again? (yes/no)")
        if input().lower().strip() == "yes":
            main()
        else:
            test == True
    
    if test == True:
        sys.exit("Goodbye!")
    

if __name__ == "__main__":
    header()
    game_instructions()
    main()
