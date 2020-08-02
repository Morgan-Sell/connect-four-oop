import numpy as np

p1_name = input('What is your name, player 1? ')
p2_name = input('What is your name, player 2? ')

token1 = 'X'
token2 = 'O'
no_token = ''

player1 = Player(p1_name, token1)
player2 = Player(p2_name, token2)

while game_over = False:
    
    p1_col_idx = input(f'{player2.name}, select a column 0 to 6. ')
    available_space = 