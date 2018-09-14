# Chessboard containing

import chesspiece
import random

file_input = 'input.txt'


class Board:
    def __init__(self):
        with open(file_input, 'rt') as f_in:
            self.pieces = []
            lines = f_in.readlines()

            for line in lines:
                line.replace('\n', '')
                row = line.split()
                for i in range(int(row[2])):
                    if row[0] == 'WHITE':
                        color = chesspiece.Chesspiece.white
                    elif row[0] == 'BLACK':
                        color = chesspiece.Chesspiece.black

                    if row[1] == 'KNIGHT':
                        pieceType = chesspiece.Chesspiece.knight
                    elif row[1] == 'BISHOP':
                        pieceType = chesspiece.Chesspiece.bishop
                    elif row[1] == 'ROOK':
                        pieceType = chesspiece.Chesspiece.rook
                    elif row[1] == 'QUEEN':
                        pieceType = chesspiece.Chesspiece.queen

                    x = random.randint(1, 8)
                    y = random.randint(1, 8)
                    while self.is_exist(x, y):
                        x = random.randint(1, 8)
                        y = random.randint(1, 8)

                    self.pieces.append(
                        chesspiece.Chesspiece(pieceType, color, x, y))

    def is_exist(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return True
        return False

    def calculate_cost(self):
        return 0

    def print_board(self):
        board = [['.' for i in range(9)] for j in range(9)]

        for piece in self.pieces:

            if piece.pieceType == chesspiece.Chesspiece.knight:
                piece_type_char = 'K'
            elif piece.pieceType == chesspiece.Chesspiece.bishop:
                piece_type_char = 'B'
            elif piece.pieceType == chesspiece.Chesspiece.rook:
                piece_type_char = 'R'
            elif piece.pieceType == chesspiece.Chesspiece.queen:
                piece_type_char = 'Q'

            if piece.color == chesspiece.Chesspiece.black:
                piece_type_char = piece_type_char.lower()

            board[piece.x][piece.y] = piece_type_char

        for i in range(1, 9):
            for j in range(1, 9):
                print(board[i][j], end=' ')
            print()
