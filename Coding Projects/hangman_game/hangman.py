"""
File: hangman.py
Name: Ilona Chuang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program simulates the game "hang man."
    If the player inputs a correct guess, the output will be updated
    If the player inputs an incorrect guess, the number of guesses left will update
    So on and so forth, until the player guesses the word or there are no guesses left
    """
    word = random_word()
    turn = N_TURNS          # turns constant to variable
    first_result = introduction(word)  # shows the word in '-' form
    hang_man(word, turn, first_result)


def introduction(word):
    """
    :param word: str, the answer to the game
    :return: str, shows the length of the answer by the amount of '-'
    """
    print('The word looks like: ', end='')
    result = ''
    for i in range(len(word)):
        result += '-'
    print(result)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    return result


def hang_man(word, turn, result):
    """
    :param word: str, the answer to the game
    :param turn: int, the amount of turns a player has in the game
    :param result: str, shows the length of the answer by the amount of '-'
    """
    while True:
        guess = input('Your guess: ')
        guess = guess.upper()                           # case insensitive
        if len(guess) != 1 or not guess.isalpha():      # the input must be an one-digit alpha
            print('illegal format.')
        else:
            if guess in word:
                new_result = ''                         # start with another empty string
                for i in range(len(word)):
                    if word[i] == guess:
                        new_result += guess             # adds correct guess to new result
                    elif result[i].isalpha():
                        new_result += result[i]         # adds previous correct guesses to new result
                    else:
                        new_result += '-'               # other indices remain as  '-'
                result = new_result
                if result == word:
                    print('You are correct!\nYou win!!')
                    print('The word was: ' + word)
                    break                               # complete answer, break loop
                print('You are correct!')               # incomplete answer
                print('The word looks like: ' + result)
                print('You have ' + str(turn) + ' guesses left.')
            else:                                       # incorrect guess
                turn -= 1
                print('There is no ' + guess + '\'s in the word.')
                if turn == 0:                           # no more guesses left, break loop
                    print('You are completely hung :(')
                    print('The word was: ' + word)
                    break
                print('The word looks like: ' + result)  # incorrect guess but there are still guesses left
                print('You have ' + str(turn) + ' guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
