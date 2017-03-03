#!/usr/bin/python

class Board:
#   initialize an n*n board:
    def __init__(self, n, hints):
        self.n = n
        self.board = [['.' for i in range(n)] for j in range(n)]
        self.hints = hints

    def __repr__(self):
        return '\n'.join(str(i) for i in self.board)
    
    def modify(self, x, y):
        self.board[x][y] = '#'
        


    
