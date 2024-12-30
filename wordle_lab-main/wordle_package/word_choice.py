import random as rd
import os
from typing import List


def read_words_file() -> List[str]:
    word_list = []
    #Read the words from the file.
    fil_path = os.path.join(os.path.dirname(__file__),"assets" ,"words.txt")
    with open(fil_path, 'r') as file:
        for line in file.readlines():
            word_list.append(line.strip())
    return word_list

def choose_random_word(words: List[str]) -> str:
    #choosing random word from the list of words
    return rd.choice(words)

def main():
    words = read_words_file()
    print(choose_random_word(words))        

if __name__ == "__main__":
    main() 
