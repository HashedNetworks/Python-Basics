import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)                  # Letter in the word
    alphabet = set(string.ascii_uppercase)    # Importing alphabet all caps
    used_letters = set()                      # Keeping track of whats already being guessed
    print(word)     
    print(alphabet)        

    while len(word_letters) > 0:
        # Telling user what letters have been used
        print('You have used these letters: ', ' '.join(used_letters))

        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input(f'Please enter letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print(f'You\'ve already used this letter')
        
        else:
            print(f'Invalid Character. Please tr again')

    # While 
            
hangman()









