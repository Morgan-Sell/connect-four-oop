import numpy as np

board_width = 7
board_height = 6

DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
)

token_color_map = {
    0 : 'white',
    1 : 'black',
    2 : 'red',
}



class Board():
    '''
    Class represent the Connect 4 board. It starts empty.
    '''
    
    def __init__(self):
        
        self.board = np.zeros((board_height, board_width))
        self.num_tokens_in_play = 0
    
    def check_rows(self, token):
        '''
        Determine if there are four tokens in a row on the rows
        
        Args:
            token (int): 1 or 2. Dependent on the player.
        Return:
            game_won (boolean): True if player has four in a row.
        '''
        tracker = []
        has_won = False
        for r in range(board_height - 1, -1, -1):
            for c in range(board_width):        
                if self.board[r][c] == token:
                    tracker.append(True)
                else:
                    tracker = []
                    
                if len(tracker) == 4 and all(tracker):
                    has_won = True
                    return has_won
        return has_won 

    def check_columns(self, token):
        '''
        Determine if there are four tokens in a row in a row.
        
        Args:
            None
        Return:
            has_won (boolean): True if player has four in a row.
       '''
        tracker = []
        has_won = False
        for c in range(board_width):
            for r in range(board_height - 1, -1, -1):
                if self.board[r][c] == token:
                    tracker.append(True)
                else:
                    tracker = []
                if len(tracker) == 4 and all(tracker):
                    has_won = True
                    return has_won
        
        return has_won 
        
   
   
    def check_for_winner(self, token, name):
        '''
        Reviews board to see if a player has four in a row.
        
        Arg:
            token (str): Character to look for.
            name(
        
        Return:
            is_winner (Boolean): Value is True if a player has four in a row.
            
        '''
        is_winner = False
        connect_4_by_row = self.check_rows(token)
        connect_4_by_column = self.check_columns(token)
        # add check_diagnol
        
        if connect_4_by_row or connect_4_by_column:
            print ('Congratulations {}! You won! Yay!'.format(name))
            is_winner = True
        
        return is_winner
            
    
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
        
        
        for r in range(board_height-1, -1, -1):
            if self.board[r][col] == 0:
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
        
class Player():
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
        
        
        
        
        