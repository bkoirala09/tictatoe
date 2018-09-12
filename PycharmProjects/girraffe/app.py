import os
import time

board = [""," "," "," "," "," "," "," "," "," "]

def print_board():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def is_winner(board , player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

def is_board_full(board):
       if " " in board:
           return False
       else:
           return True


while True:
    print_board()

    #user input for X
    choice = input("Choose an empty space for X")
    choice = int(choice)


    # check to see if the board is empty first
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("The space is already taken")
        time.sleep(2)



    #check for X win
    if is_winner(board , "X"):
        os.system("clear")
        print_board()
        print("Congratulations : X wins")
        break

    print_board()

    # check for a tie
    #if board is full
    if is_board_full(board):
        print("Tie !")
        break



    # user input 0
    choice = input("Choose an empty space for 0")
    choice = int(choice)

    # check to see if the board is empty first
    if board[choice] == " ":
        board[choice] = "0"
    else:
        print("The space is already taken")
        time.sleep(2)

    # check for 0 win
    if  is_winner(board , "0"):
        os.system("clear")
        print_board()
        print("Congratulations : 0 wins")
        break

    # check for a tie
    #if board is full
    if is_board_full(board):
        print("Tie !")
        print("Hwllo")
        break





