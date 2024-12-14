from token import Tokens
class Board():
    def __init__(self):
        self.board = [[Tokens.empty for i in range(3)] for j in range(3)]
        self.moves = 0
    def is_full(self):
        return self.moves == 9
    def make_move(self,i,j,tokens:Tokens):
        if self.is_full():
            raise ValueError("board is full")
        if not (0 <= i < 3 and 0 <= j < 3) or self.board[i][j]!=Tokens.empty:
            raise ValueError("Invalid position")
        self.board
            
