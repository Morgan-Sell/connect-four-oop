import numpy as np
from connectfour import Board, Player
import pygame
import sys

game_over = False

no_token = 0
p1_token = 1
p2_token = 2

blue = (0, 0, 255)
column_count = 7
row_count = 6
square_size = 100
#board_width = column_count * square_size
#board_height = row_count * square_size

p1_name = input('Player 1 Name: ')
p2_name = input('Player 2 Name: ')

player1 = Player(p1_name, p1_token)
player2 = Player(p2_name, p2_token)
board = Board(column_count, row_count, square_size)

board.draw_board(blue)


'''

while game_over == False:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:    
            # PLAYER ONE'S TURN
            p1_col = int(input(f'{p1_name}, select a column to drop a token. Options are 0 to {board_width-1}. ' ' ))
            available_space = board.is_valid_loc(p1_col)

            # Ask to select another column if space is not available.
            while available_space == False:
                print('Ooops! The column that you selected is full.')
                p1_col = int(input(f'Select a different column. Options are 0 to {board_width-1}.' ))
                available_space = board.is_valid_loc(p1_col)

            avail_row = board.find_first_available_row(p1_col)
            board.update_board(avail_row, p1_col, p1_token)
            print(board.board)

            # Check if Player 1 won
            game_over = board.check_for_winner(player1.token, player1.name)
            if game_over:
                break

            # PLAYER TWO'S TURN
            p2_col = int(input(f'{p2_name}, select a column to drop a token. Options are 0 to {board_width-1}. ' ))
            available_space = board.is_valid_loc(p2_col)

            # Ask to select another column if space is not available.
            while available_space == False:
                print('Ooops! The column that you selected is full.')
                p2_col = int(input(f'Select a different column. Options are 0 to {board_width-1}.' ))
                available_space = board.is_valid_loc(p2_col)

            avail_row = board.find_first_available_row(p2_col)
            board.update_board(avail_row, p2_col, p2_token)
            print(board.board)

            game_over = board.check_for_winner(player2.token, player2.name)
'''