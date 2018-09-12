# Thomas J Lee
# Project: Spaceman (Hangman)

# Requirements:
# 1) If the guessed letter is in the mystery word, the position(s)
# of the letter(s) are revealed in the placeholders.

# 2) If a guessed letter occurs more than once in the word all
# the places that letter occurs are revealed.

# 3) If a player guesses all the letters in the word, they win the game.

# 4) For each incorrect guess a part of the Spaceman (a 7 part drawing
# of a Spaceman) is drawn.

# If all 7 parts of the Spaceman are drawn then the player loses.

# Code Requirements:
# Variable assignment
# Function definitions
# Core data types: strings, integers, floats
# Collection types: lists, tuples, dictionary

import random

def count_check(count):
    if counter >= 7:
        print("You lose! Better luck next time!")
        return

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   start_word = ""
   start_word = secret_word

   return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secret_list = list(secret_word)
    for i in secret_list:
        if i not in letters_guessed:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user hasnot yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...

    underscore = []
    for i in range(0, len(secret_word)):
        if secret_word[i] in letters_guessed:
            underscore.append(secret_word[i])
        else:
            underscore.append("_")

    return underscore

    # print("Wrong guess! You have {} guesses left!".format(counter))


def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    arr = [letters_guessed]
    return arr


def user_input(prompt):
    user_input = input(prompt)
    return user_input

def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how man\y
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...

    count = 0
    guesses = []

    print("Welcome to Spaceman! The secret word contains {} letters!".format(len(load_word())))
    print("Please guess 1 letter at a time!")
    print("If you exceed 7 guesses you lose!")

    while count <= 7:
        guess1 = user_input('Guess letter: ')
        guesses.append(guess1)
        if is_word_guessed(secret_word, str(guesses)):
            get_guessed_word(secret_word, guesses)
            print(secret_word)
            print("You win Spaceman!")
            count = 8

        else:
            print_word = get_guessed_word(secret_word, str(guesses))
            print("You lose Spaceman :(")
            print(print_word)

# spaceman(load_word())
spaceman("Tom")


#
# secret_word = load_word()
# spaceman(load_word())
