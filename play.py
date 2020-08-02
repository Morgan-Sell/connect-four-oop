import numpy as np
from connect-four import game

game_over = False

p1_name = input('Player 1 Name: ')
p2_name = input('Player 2 Name: ')

p1_token = 'X'
p2_token = 'O'
no_token= ' '


player1 = Player(p1_name, p1_token)
player2 = Player(p2_name, p2_token)

board = Board()



while game_over = False:
    
    p1_col_idx = input(f'{p1_name} select a column 0 to 5 to drop a token': )
    available_space = player1.drop_token(p1_col_idx)
    # If player 1 se
    while available_space == False:
        print('No available space. Select another column')
        p1_col_idx = input(f'{p1_name} select a column 0 to 5 to drop a token': )
        available_space = p1_name.drop_token(p1_col_idx)
        
    # check if player 1 won
    
    # Player 2
    
    # If player 2 did not select a column with space available for a token.
    p2_col_idx = input(f'{p2_name} select a column 0 to 5 to drop a token': )
    available_space = player2.drop_token(p1_col_idx)
    
    # If player 2 did not select a column with space available for a token.
    while available_space == False:
        print('No available space. Select another column')
        p2_col_idx = input(f'{p2_name} select a column 0 to 5 to drop a token': )
        available_space = player2.drop_token(p2_col_idx)
    
    # Check if player 2 won.