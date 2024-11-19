# Connect Four - Lab 5B

### Author: Sabrina Joseph  
### Date: 02-28-2024  
### Last Modified: 02-28-2024

## Description
This project was a lab assignment for my **Programming 1 Fundamentals class** at the **University of Florida**.  

This Python script implements a simple version of the classic Connect Four game. Players take turns to drop "chips" (represented by `x` and `o`) into a grid and aim to get four in a row, either horizontally or vertically. The game board size is configurable based on user input.

## Features
- Customizable board size (height and length).
- Two players take turns placing their chips on the board.
- The game checks for a winner (4 chips in a row, horizontally or vertically).
- The game also checks for a draw if the board is full and no winner is found.

## Functions
### `print_board(board)`
This function visually prints the current state of the game board to the console. It reverses the board for correct visual representation, as the bottom row is printed first.

### `initialize_board(num_rows, num_cols)`
Initializes the game board as a 2D list with the specified number of rows and columns, using `"-"` to represent empty spaces.

### `insert_chip(board, col, chip_type)`
Inserts a chip (either `x` or `o`) into the specified column on the board. The chip will fall to the lowest available row in that column.

### `check_if_winner(board, col, row, chip_type)`
Checks if the player who just made a move has won the game by getting 4 chips in a row, either horizontally or vertically.

### `is_board_full(board)`
Checks if the board is full (no empty spaces left), in which case the game results in a draw.

## How to Use
1. Run the script in a Python environment.
2. The program will prompt you to input the desired height and length for the board.
3. Players will alternate choosing a column to drop their chips into.
4. The game will continue until one player gets four chips in a row or the board is full.

## Example Usage
```plaintext
What would you like the height of the board to be? 6
What would you like the length of the board to be? 7
Player 1: x
Player 2: o

Player 1: Which column would you like to choose? 3
-  -  x  -  -  -  -

Player 2: Which column would you like to choose? 4
-  -  x  o  -  -  -

...(game continues)
```
## License
This project is licensed under the MIT License. See the LICENSE file for details.
