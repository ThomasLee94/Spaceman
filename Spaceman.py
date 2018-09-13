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

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   start_word = ""
   start_word = secret_word

   print("Start word: {}".format(start_word))
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

    letter_or_underscore = []
    for i in range(0, len(secret_word)):
        if secret_word[i] in letters_guessed:
            letter_or_underscore.append(secret_word[i])
        else:
            letter_or_underscore.append("_")
    return letter_or_underscore

    # print("Wrong guess! You have {s} guesses left!".format(counter))


def is_correct_guess(secret_word, letters_guessed):
    # if letters_guessed in secret_word:
    #     return True
    # else:
    #     return False
    
    if len(letters_guessed)>0:
        if letters_guessed[-1] in list(secret_word):
            print("TRUE")
            return True
        else:
            print("FALSE")
            return False
    else:
        print("No guesses found!")


def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    arr = [letters_guessed]
    return arr


def user_input(prompt):
    valid_input = False
    user_guess = ""
    while valid_input == False:
        user_guess = input(prompt)

        if len(user_guess) == 1:
            valid_input = True
        else:
            print("Please only enter one letter, try again")

        print("does this work")

    return user_guess




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
    guesses_list = []

    print("Welcome to Spaceman! The secret word contains {} letters!".format(len(secret_word)))
    print("Please guess 1 letter at a time!")
    print("If you exceed 7 guesses you lose!")
    # Perhaps rename to game_board
    game_board = get_guessed_word(secret_word, str(guesses_list))
    print(game_board)
    # print("HERE: {}".format(show_underscore))


    # secret_word = "cat"

    while count < 7:
        guess = user_input('Guess letter: ')
        guesses_list.append(guess)

        print_word = get_guessed_word(secret_word, str(guesses_list))

        # As gueses happen, redraw the board
        print("{}".format(print_word))

        if is_correct_guess(secret_word, guesses_list) == False:
            count += 1
        else:
            count = count

        print(count)


        # Win Game.
        if is_word_guessed(secret_word, str(guesses_list)):
            get_guessed_word(secret_word, guesses_list)
            print(secret_word)
            print("You WIN Spaceman!")
            return

    # Lose Game.
    if count > 7:
        print("Loser")
        return


spaceman(load_word())
#is_correct_guess("cat", "a")


#
# secret_word = load_word()
# spaceman(load_word())
