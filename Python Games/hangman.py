import random
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)               # Choosing word from dictionary
    word_list = list(word)                     # Converting text into list
    word_len = len(word)                       # Getting list lenght
    word_guess = ['-']*word_len                # Initializing list for Hangman word to guess
    list_str = ' '.join(map(str, word_guess))  # Convert list into text
    dup_let_pos = []
    list_str_2= ''
    print(list_str)
    print(word)

    while word != list_str_2:


        ask_letter = input("Please enter a letter: ").upper()
        count_letter = word_list.count(ask_letter)

        if count_letter > 1:                                    # if letter is dupplicated
            for i in range(word_len):                           # For-loop looking for dup letter position in list 
                if ask_letter == word_list[i]:                  # Saving indexes for dup letters
                    dup_let_pos.append(i)                       # Appending positions into new list
            for pos in range(len(dup_let_pos)):                 # For-loop looking to add duplicate letters in secret word
                word_guess[dup_let_pos[pos]] = ask_letter       # Adding dup letter in secret word
                list_str_2 = ' '.join(map(str, word_guess))     # Converting new list into str
            print(list_str_2)                                   # printing dup letters in secret word

        if count_letter == 1:                                           # if letter is not dup
            if ask_letter in word_list:                                  
                word_guess[word_list.index(ask_letter)] = ask_letter
                list_str_2 = ''.join(map(str, word_guess))
                print(list_str_2)

    print(f'You\'ve found the word')


hangman()