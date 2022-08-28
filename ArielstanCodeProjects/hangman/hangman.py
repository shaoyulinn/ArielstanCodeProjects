"""
File: hangman.py
Name: Ariel
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
    This program runs the Hangman Game.
    """
    answer = random_word()
    print('THe word looks like ', end='')
    for i in range(len(answer)):
        print('-', end='')
    print('')

    a = N_TURNS
    # We use this variable to count how many wrong guesses are left
    guess = ''
    for i in range(len(answer)):
        guess += str('-')

    while True:
        new_guess = ''
        # This variable records the guess we make
        print('You have '+str(a)+' wrong guesses left.')
        input_ch = input('Your guess: ')
        if not input_ch.isalpha():
            print('Illegal format.')
            input_ch = input('Your guess: ')
        if len(input_ch) != 1:
            print('Illegal format.')
            input_ch = input('Your guess: ')

        for i in range(len(answer)):
            ch = answer[i]
            if input_ch.upper() == ch:
                new_guess += ch
            else:
                new_guess += guess[i]

        if new_guess == answer:   # Win
            break

        if guess == new_guess:
            print('There is no '+input_ch.upper()+"'s in the word.")
            a -= 1
            if a == 0:   # Run out of guesses
                break
        else:
            print('You are correct!')

        print('The word looks like '+new_guess)
        guess = new_guess

    if new_guess == answer:
        print('You are correct!')
        print('You win!!')
    else:
        print('There is no ' + input_ch.upper() + "'s in the word.")
        print('You are completely hung : (')
    print('The word was: '+answer)


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
