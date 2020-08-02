import numpy as np
from connectfour import Board, Player

game_over = False

p1_name = input('Player 1 Name: ')
p2_name = input('Player 2 Name: ')

no_token = 0
p1_token = 1
p2_token = 2

player1 = Player(p1_name, p1_token)
player2 = Player(p2_name, p2_token)
board = Board()



while game_over = False:
    
    # PLAYER ONE'S TURN
    p1_col = int(input(f'{p1_name} select a column 0 to 5 to drop a token': ))
    available_space = board.is_valid_loc(p1_col)
    
    # Ask to select another column if space is not available.
    while available_space == False:
        print('No available space. Select another column')
        p1_col_idx = int(input(f'{p1_name} select a column 0 to 5 to drop a token': ))
        available_space = board.is_valid_loc(p1_col)
    
    avail_row = board.find_first_available_row(self, p1_col)
    
    board.update_board(avail_row, p1_col, p1_token)
    player1.add_token_pos((avail_row, p1_col))
    
    
    # check if player 1 won
    
    # Player 2
    
    # If player 2 did not select a column with space available for a token.
    p2_col_idx = int(input(f'{p2_name} select a column 0 to 5 to drop a token': ))
    available_space = player2.drop_token(p1_col_idx)
    
    # If player 2 did not select a column with space available for a token.
    while available_space == False:
        print('No available space. Select another column')
        p2_col_idx = input(f'{p2_name} select a column 0 to 5 to drop a token': )
        available_space = player2.drop_token(p2_col_idx)
    
    # Check if player 2 won.