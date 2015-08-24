#!/usr/bin/env python
# Exercise: seventeen0.py  
# Write a program to:
# Play a game where a human and a computer remove marbles from a jar (either
# 1, 2, or 3 marbles per turn) starting with 17 marbles.  The human and 
# computer aleternate turns.  An error message should be displayed if the human
# guesses a number outside of the 1-3 range.  
##############################################################################
import sys
import random

def validate_guess(guess, marbles):
   """This function accepts a string user guess, and an integer representing the
   number of marbles remaining as arguments.  From there, the function validates that
   the user guess is an integer within an acceptable range, and returns an integer
   representing their guess.
   """
    
   while True:
        try:
            test = int(guess)
            if test != 1 and test != 2 and test != 3 or test > marbles:
                raise ValueError
        except Exception:
            print "Sorry that is not a valid option.  Try again."
            print_marbles(marbles)
            guess = raw_input("Your turn.  How many marbles will you remove (1-3)? ")
            continue
        return test


def start_game():
    """ Short function to start the game.  Sets the 'jar' to contain 17 marbles, 
    prints an opening message, and returns the 17 marbles.
    """

    marbles = 17
    print "Let's play the game of seventeen"
    print_marbles(marbles)
    return marbles


def print_marbles(marbles):
    # This function serves to reduce the amount of times this print
    # statement needs to be written.

    print "Number of marbles left in jar: {0}".format(marbles)
    print ""


def computer_guess(marbles):
    """ This function accepts the remaining number of marbles as an argument,
    allows the computer to make a random selection of marbles to remove, and 
    returns the remainng number of marbles.
    """

    max_selection = 3
    marbs = marbles

    if marbs < 3:
        max_selection = marbs

    print "Computer's turn..."
    comp_selection = random.randint(1, max_selection)
    print "Computer removed {0} marbles.".format(comp_selection)
    marbs = marbs - comp_selection
    if marbs == 0:
        game_over("Human player")
    elif marbs > 0:
        print_marbles(marbs)

    return marbs 


def game_over(s):
    # Brief function which runs when marbles = 0 (game over).
    print ""
    print "There are no marbles left.  {0} wins!".format(s)
    sys.exit()

def user_guess(marbles):
    """ This function prompts the user to make a selection of marbles out
    of the jar, accepting marbles as its argument.  The user selection is
    verified, information is printed to the user, and the remaining number 
    of marbles is returned (as long as the game is continuing).
    """
    
    marbs = marbles
    guess = raw_input("Your turn.  How many marbles will you remove (1-3)? " )
    final_guess = validate_guess(guess, marbs)
    print "You removed {0} marbles.".format(final_guess)
    marbs = marbs - final_guess
    if marbs == 0:
        game_over("Computer")
    elif marbs > 0:
        print_marbles(marbs)

    return marbs


def play_game():
    marbles = start_game()
    while marbles > 0:
        marbles = user_guess(marbles)
        marbles = computer_guess(marbles)

##############################################################################
def main():  # CALL YOUR FUNCTION BELOW
    play_game()

if __name__ == '__main__':
    main()