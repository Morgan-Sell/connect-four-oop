import numpy as np

board_width = 7
board_height = 6

DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
)

token_color_map = {
    p1_token : 'black'
    p2_token : 'red'
    no_token : 'white'
}



class Board(self):
    '''
    Class represent the Connect 4 board. It starts empty.
    '''
    
    def __init__(self):
        
        self.board = np.zeros((board_width, board_height))
   
    def check_for_winner(self, token):
        '''
        Reviews board to see if a player has four in a row.
        
        Arg:
            token (str): Character to look for.
        
        Return:
            found_winner (Boolean): Value is True if a player has four in a row.
        '''
     
    
    def is_valid_loc(self, col):
        '''
        Check if space is available
        
        Args:
            col (int): column selected by player
        Returns:
            available (Boolean): True if space is available
        '''
        if self.board[0][col] == 0:
            available = True
        else:
            available = False
        
        return available
    
    
    def find_first_available_row(self, col):
        '''
        Find the row where the token will land.
        
        Args:
            col (int): column selected by player
        Returns:
            row_idx (int): Row # where token will land.
        '''
        
        
        for r in range(board_height, -1, -1):
            if self.board[r][col] == 0
                row_idx = r
                break
        
        return row_idx
    
    def update_board(self, row, col, token):
        '''
        Update the board coordinate with the appropriate token.
        
        Args:
            loc (tuple): Board coordinates
            token (int): 1 or depending on the player
         
        Return:
            None
        '''
        self.board[row][col] = token
        
class Player(self):
    # One of two players who can play Connect 4.
    
    def __init__(self, name, token):
        
        self.name = name
        self.token = token
        self.pos_of_tokens = []
    
    
        
    def add_token_pos(self, loc):
        '''
        Adds token to a list of the locations of the player's tokens on the board.
        
        Args:
            loc (tuple) : location (row, column) of a token added by a player.
            
        Return:
            None
        '''
        
        self.pos_of_tokens.append(loc)
        
        
        
        
        