"""
Author: Sabrina Joseph
Date: 02-28-2024
Last Modified: 02-28-2024
Description: Lab 5B - Connect Four
"""

# function for my visual representation of my board
def print_board(board):
    reversed_board = board[::-1]  # This line in particular reverses the board
    for i in range(len(reversed_board)):
        for j in range(len(reversed_board[i])):
            print(reversed_board[i][j], " ", end="")
        print()

# function for my behind the scene 2D array
def initialize_board(num_rows, num_cols):
    board = []
    for i in range(num_rows):
        board.append(["-" for j in range(num_cols)])
    return board

# this is the function to actually serve as the placement for the "x" and "o" chips
def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == "-":
            board[row][col] = chip_type
            return

# checks if there is a horizontal and/or vertical win
def check_if_winner(board, col, row, chip_type):
    # This will check for a horizontal winner
    count = 0
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # This will check for a vertical winner
    count = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False

# This checks for if there is a tie
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == "-":
                return False
    return True

def main():
    # getting the desired height and length from the user
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))

    # this is taking in the values to create an array and storing it in the variable name "game_board"
    game_board = initialize_board(height, length)
    # using the print_board function with the variable game_board to create a user-friendly visual board
    print_board(game_board)
    print("\nPlayer 1: x")
    print("Player 2: o")

    # setting player 1 as the default player
    player = 1
    while True:
        player_choice = int(input(f"\nPlayer {player}: Which column would you like to choose? "))
        insert_chip(game_board, player_choice, "x" if player == 1 else "o")
        print_board(game_board)
        # This is checking if there is 4 in a row
        if check_if_winner(game_board, player_choice, len(game_board) - 1, "x" if player == 1 else "o"):
            print(f"\nPlayer {player} won the game!")
            break
        # This is checking for if the board is full
        elif is_board_full(game_board):
            print("\nDraw. Nobody wins.")
            break
        player = 3 - player


if __name__ == "__main__":
    main()
