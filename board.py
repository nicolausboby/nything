# Chessboard berisi kelas Board

import chesspiece
import random

file_input = 'input.txt'

# Kelas Board merepresentasikan papan catur
# yang akan digunakan dalam pemecahan masalah


class Board:
    # Konstruktor Board melakukan pembacaan file input
    # dan inisialisasi board awal secara acak
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
                        piece_type = chesspiece.Chesspiece.knight
                    elif row[1] == 'BISHOP':
                        piece_type = chesspiece.Chesspiece.bishop
                    elif row[1] == 'ROOK':
                        piece_type = chesspiece.Chesspiece.rook
                    elif row[1] == 'QUEEN':
                        piece_type = chesspiece.Chesspiece.queen

                    x = random.randint(1, 8)
                    y = random.randint(1, 8)
                    while self.is_exist(x, y):
                        x = random.randint(1, 8)
                        y = random.randint(1, 8)

                    self.pieces.append(
                        chesspiece.Chesspiece(piece_type, color, x, y))

    # randomize_pieces melakukan pengacakan terhadap posisi pieces
    def randomize_pieces(self):
        old_pieces = self.pieces
        self.pieces = []

        for piece in old_pieces:
            color = piece.color
            piece_type = piece.piece_type
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            while self.is_exist(x, y):
                x = random.randint(1, 8)
                y = random.randint(1, 8)
            self.pieces.append(
                chesspiece.Chesspiece(piece_type, color, x, y))

    # is_exist mengembalikan True jika terdapat sebuah piece pada x,y dalam board
    def is_exist(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return True
        return False

    # calculate_cost mengembalikan total cost dari suatu kondisi board
    def calculate_cost(self):
        return self.same_color_cost() - self.diff_color_point()

    # same_color_cost mengembalikan total nilai cost dari pieces yang berwarna sama
    def same_color_cost(self):
        total = 0
        for piece in self.pieces:
            for other_piece in self.pieces:
                if piece != other_piece and piece.color == other_piece.color and piece.can_attack(other_piece.x, other_piece.y):
                    total = total + 1

        return total

    # diff_color_point mengembalikan total nilai poin dari pieces yang berwarna berbeda
    def diff_color_point(self):
        total = 0
        for piece in self.pieces:
            for other_piece in self.pieces:
                if piece != other_piece and piece.color != other_piece.color and piece.can_attack(other_piece.x, other_piece.y):
                    total = total + 1

        return total

    # print_board mencetak board pada layar
    def print_board(self):
        board = [['.' for i in range(9)] for j in range(9)]

        for piece in self.pieces:
            if piece.piece_type == chesspiece.Chesspiece.knight:
                piece_type_char = 'K'
            elif piece.piece_type == chesspiece.Chesspiece.bishop:
                piece_type_char = 'B'
            elif piece.piece_type == chesspiece.Chesspiece.rook:
                piece_type_char = 'R'
            elif piece.piece_type == chesspiece.Chesspiece.queen:
                piece_type_char = 'Q'

            if piece.color == chesspiece.Chesspiece.black:
                piece_type_char = piece_type_char.lower()

            board[piece.x][piece.y] = piece_type_char

        for i in range(8, 0, -1):
            for j in range(1, 9):
                print(board[j][i], end=' ')
            print()
        print('\n', self.same_color_cost(), '\t', self.diff_color_point())
