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
        
        self.board = np.empty((board_width, board_height))
   
    def check_for_winner(self):
        
        
class Player(self):
    # One of two players who can play Connect 4.
    
    def __init__(self, name, token):
        
        self.name = name
        self.token = token
        self.pos_of_tokens = []
    
    def drop_piece(self, col_idx):
        '''
        Attempts to drop token in selected column. Returns True if able to drop piece.
        
        Args:
            col_idx (int): The board column that the player selects to drop the piece.
            
        Return:
            space_avail (boolean): Tells game there is available space for a token in the selected column.
        '''
        
        for r in range(board_height, -1, -1):
            if self.board[r, col_idx] == '':
                self.board[r.col_idx] = self.token
                self.add_token_pos((r, col_idx))
                return True
        
        return False
        
    def add_token_pos(self, loc):
        '''
        Adds token to a list of the locations of the player's tokens on the board.
        
        Args:
            loc (tuple) : location (row, column) of a token added by a player.
            
        Return:
            None
        '''
        
        self.pos_of_tokens.append(loc)
        
        
        
        
        