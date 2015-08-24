#!/usr/bin/env python
# Exercise: seventeen0.py  
# Write a program to:
# Play a game where a human and a computer remove marbles from a jar (either
# 1, 2, or 3 marbles per turn) starting with 17 marbles.  The human and 
# computer aleternate turns.  In this version of the game, the human is replaced
# by a text file of moves to be executed by 'Player 1' in sequence. 
##############################################################################

import sys
import random


def start_game():
    """ Short function to start the game.  Sets the 'jar' to contain 17 marbles, 
    prints an opening message, and returns the 17 marbles.
    """

    marbles = 17
    return marbles



def computer_guess(marbles, list_, play_sequence, game):
    """ This function accepts the remaining number of marbles as an argument,
    an updated list of marbles removed in each turn up to the present move, 
    the sequence of moves for Player 1, and the game number as arguments.  The
    computer then selects a random number of marbles to remove, and if there
    are still marbles in play that number of marbles, the updated list of 
    removed marbles by turn, and the Player 1 sequence are returned.
    """

    max_selection = 3
    marbs = marbles


    if marbs < 3:
        max_selection = marbs

    if marbs > 1:
        comp_selection = random.randint(1, max_selection)
    else:
        comp_selection = 1
    marbs = marbs - comp_selection
    list_.append(comp_selection)
    if marbs == 0:
        game_over("Winner: P1", list_, game)


    return marbs, list_, play_sequence 


def game_over(s, game_sequence, game):
    """Function accepts an string, the final sequence of plays from the just completed
    game, and the game number as arguments.  The function doesn't return anything, but
    opens a text file to write the results oof the game to the file.
    """
    beginning = "Game #{0}.  ".format(game)
    game_str = "Play sequence: " + '-'.join(str(x) for x in game_sequence) + ".  " + s
    with open("i206_placein_output_ehagen.txt", 'a') as f:
        f.write(beginning + game_str + "\n")


def generate_user_list(game_num):
    """This function accepts the game number as an argument.  The function opens
    a text file and finds the correspending line number in the file to get the moves
    to be executed by Player 1.  The function returns that sequence of moves as a
    list.
    """

    user_list = []
    with open("i206_placein_input.txt", 'r') as f:
        for index, line in enumerate(f):
            if index == (game_num-1):
                user_list = line.strip()
                user_list = user_list.replace(',', '')
                return list(user_list)

def get_file_length():
    """This function opens the text file of Player 1 marble decisions, and counts
    the number of lines of input in the file.  This determines how many 'games' will
    be played by the program.  The number of games is returned.
    """

    game_length = 0
    with open("i206_placein_input.txt", 'r') as f:
        for index, line in enumerate(f):
            game_length += 1
    return game_length

def user_guess(marbles, list_, play_sequence, game):
    """ This function accepts the number of marbles left, a list of marbles removed
    by turn to this point, the sequence of moves for Player 1 to execute, and the 
    game number as arguments.  The function executes the next 'move' in the Player 1
    sequence, and as long as the game isn't over, returns the number of marbles 
    remaining, the sequence of moves by each player up to this point, and the game
    number.
    """
    
    user_sequence = play_sequence
    marbs = marbles
    game_sequence = []
    game_sequence = list_
    x = int(user_sequence.pop(0))
    if x > marbs:
        x = marbs
    marbs = marbs - x
    game_sequence.append(x)
    if marbs == 0:
        game_over("Winner: P2", game_sequence, game)



    return marbs, game_sequence, user_sequence



def play_game():
    """This function is used to control the gameplay.  A new text file is created,
    wins by each player are tracked, as the game is played for each line of moves
    in the text file.  The results of each game are written to a new text file, with
    an end of program summary printed as the last line of the file.
    """

    with open("i206_placein_output_ehagen.txt", 'wb') as file_:
        pass
    p1_wins = 0
    p2_wins = 0
    # For loop to ensure all 'games' of data are run from the input text file.
    for game in range(1, get_file_length()+1):
        marbles = start_game()
        list_=[]
        play_sequence=generate_user_list(game)
        # While loop runs for each individual game in the range of games.
        while marbles > 0:
            marbles, list_, play_sequence = user_guess(marbles, list_, play_sequence, game)
            marbles, list_, play_sequence = computer_guess(marbles, list_, play_sequence, game)
    # I'm reading the text file of results to find how many times each player won.
    with open("i206_placein_output_ehagen.txt", 'r') as fin:
        data = fin.readlines()
        for line in data:
            p2_wins += line.count("P2")
            p1_wins += line.count("P1")
    
    closing_sentence = "Player 1 won {0} times; Player 2 won {1} times.".format(p1_wins, p2_wins)
    with open("i206_placein_output_ehagen.txt", 'a') as f:
        f.write(closing_sentence)

##############################################################################
def main():  # CALL YOUR FUNCTION BELOW
    play_game()


if __name__ == '__main__':
    main()