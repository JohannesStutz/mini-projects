"""Ultra-simple HANGMAN game. The hidden word is hard-coded into the file."""

import string
from time import sleep

max_wrong = 3 # how many letters are allowed to be guessed wrong ("how many lines does the man have?")
word = 'QUARANTINE' # All CAPS!
to_guess = set(word) # only unique letters matter -> set
hit = []
miss = []

def show_word():
    """This function prints a reduced version of the word,
    it replaces letters that are not guessed yet with underscores.
    """
    output = ['_' if l not in hit else l for l in word]
    print(' '.join(output))
    
def show_full_word():
    print(' '.join(word))

def show_wrong_guesses():
    print(' '.join(miss))

def guess():
    """This function asks the user input to input his guess. (Then transforms this to UPPERCASE)
    If the input string is longer than 1 letter, it's assumed that the player guesses the full word.
    If he is correct, to_guess is cleared, therefore the player wins.
    """
    guess = input('Which letter do you want to try?\n').upper() 
    
    if len(guess) > 1:
        if guess == word:
            to_guess.clear()
        return guess
    
    # If the input is not in [A-Z], ask the player again
    while guess not in string.ascii_uppercase:
        guess = input('That was not a letter. Which letter do you want to try?\n').upper() 
        
    return guess
    
    
def play():
    turns = max_wrong
   
    print('Welcome to HANGMAN! Try to guess the hidden word.')
    print('Use one letter at a time, unless you are sure you know the word.')
    
    while turns > 0 and to_guess:
        print('\n\n')
        print('You\'ve got '+str(turns)+' misses left')
        show_word()
        
        # To avoid the input appearing before the rest of the content, wait for 0.1s
        sleep(0.1)
        letter = guess()
        
        if letter in hit or letter in miss:
            print('You already guessed that letter')
            print('These are letters that are NOT in the word:')
            show_wrong_guesses()
        elif letter in to_guess:
            hit.append(letter)
            to_guess.remove(letter)
        else:
            miss.append(letter)
            turns -= 1
    else:
        if not to_guess:
            print('\nCongratulations, you won!')
        else:
            print('\nSorry, you lost. The word was:')
        show_full_word()
    
play()