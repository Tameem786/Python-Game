# Tic Tac Toe
from os import system, name
import random
import time


def screen_clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def display_board(board):
    screen_clear()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose X or O: ").upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):

    return((board[1] == mark and board[2] == mark and board[3] == mark)or
           (board[4] == mark and board[5] == mark and board[6] == mark)or
           (board[7] == mark and board[8] == mark and board[9] == mark)or
           (board[1] == mark and board[4] == mark and board[7] == mark)or
           (board[2] == mark and board[5] == mark and board[8] == mark)or
           (board[3] == mark and board[6] == mark and board[9] == mark)or
           (board[1] == mark and board[5] == mark and board[9] == mark)or
           (board[3] == mark and board[5] == mark and board[7] == mark))


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == '.'


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, turn):

    position = int(input(turn + ":Choose a position: (1-9) "))
    return position


def replay():
    choice = input("Play Again: Type Yes or No? ")
    return choice == 'yes'


# Main Code
blank = []

print("Welcome to Tic Tac Toe")


while True:

    the_board = ['.']*10

    player1_marker, player2_marker = player_input()

    turn = choose_first()

    print(turn + ' will go first.')
    play_game = input("Ready to play? y or n? ")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(the_board)

            position = player_choice(the_board, turn)

            if position in blank:
                print("Enter unique number.This block has been filled")
                time.sleep(5)
                turn = 'Player 1'

            else:
                blank.append(position)

                place_marker(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print('Player 1 has Won!!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("Tie Game...")
                        game_on = False
                    else:
                        turn = 'Player 2'

        else:
            display_board(the_board)

            position = player_choice(the_board, turn)

            if position in blank:
                print("Enter unique number.This block has been filled")
                time.sleep(5)
                turn = 'Player 2'

            else:
                blank.append(position)

                place_marker(the_board, player2_marker, position)

                # display_board(the_board)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2 has Won!!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("Tie Game...")
                        game_on = False
                    else:
                        turn = 'Player 1'

    if not replay():
        break
