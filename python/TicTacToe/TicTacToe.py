from abc import ABC
from board import Board
class TicTacToe():
    def __init__(self):
        self.board = Board
    
    def show_board(self):
        for i in range(3):
            print(self.board[i],'\n')
    def add_player1():
        