# Chessboard berisi kelas Board

import chesspiece
import random

file_input = 'input.txt'


# Kelas Board merepresentasikan papan catur
# yang akan digunakan dalam pemecahan masalah


class Board:
    # Konstruktor Board melakukan pembacaan file input
    # dan inisialisasi board awal secara acak
    def __init__(self, pieces=None):
        if pieces is None:
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

        else:
            self.pieces = pieces

    def __repr__(self):
        """
        :return: string representation of object board in pieces list
        """
        return str(self.pieces)

    def randomize_pieces(self):
        """ randomize the state of pieces on board
        :return: None
        """
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

    def mutate(self):
        """ move one chess piece on the board to random cell
        :return: Nothing
        """
        piece_idx = random.randint(0, len(self.pieces) - 1)
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        while self.is_exist(x, y):
            x = random.randint(1, 8)
            y = random.randint(1, 8)
        self.pieces[piece_idx].x = x
        self.pieces[piece_idx].y = y

    def is_exist(self, x, y):
        """ checks if a chess piece is currently in the position x, y
        :param x: position on the x axis
        :param y: position on the y axis
        :return: True if there is a piece in x, y, otherwise return False
        """
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return True
        return False

    def have_conflicts(self):
        """ checks if there are two pieces on the same cell
        :return: True if there are more than one piece on the same cell
        """
        locations = set()
        for piece in self.pieces:
            if (piece.x, piece.y) in locations:
                return True
            else:
                locations.add((piece.x, piece.y))
        return False

    def calculate_cost(self):
        """ calculate the total cost of the board
        :return:
        """
        return self.same_color_cost() - self.diff_color_point()

    def calculate_max_cost(self):
        """ calculate the possible maximum cost of the board
        :return:
        """
        white_piece_count = sum(1 if piece.color == chesspiece.Chesspiece.white else 0 \
                for piece in self.pieces if piece.color == chesspiece.Chesspiece.white)
        black_piece_count = len(self.pieces) - white_piece_count
        assert(white_piece_count > 0 or black_piece_count > 0)
        white_max_cost = white_piece_count * (white_piece_count - 1) if white_piece_count > 1 else 1
        black_max_cost = black_piece_count * (black_piece_count - 1) if black_piece_count > 1 else 1
        return white_max_cost + black_max_cost

    # same_color_cost mengembalikan total nilai cost dari pieces yang berwarna sama
    def same_color_cost(self):
        total = 0
        for piece in self.pieces:
            for other_piece in self.pieces:
                if piece != other_piece and piece.color == other_piece.color and piece.can_attack(
                        other_piece.x, other_piece.y) and not self.is_path_blocked(piece, other_piece):
                    total = total + 1

        return total

    def is_path_blocked(self, piece, other_piece):
        """ I.S : piece can attack other_piece
        :param piece: current piece for path checking
        :param other_piece: tested attacked piece
        :return: True if there is a blocking piece in current piece path to other_piece, otherwise return false
        """
        if piece.piece_type == chesspiece.Chesspiece.knight:
            return False

        if piece.x > other_piece.x:
            delta_x = -1
        elif piece.x < other_piece.x:
            delta_x = 1
        else:
            delta_x = 0

        if piece.y > other_piece.y:
            delta_y = -1
        elif piece.y < other_piece.y:
            delta_y = 1
        else:
            delta_y = 0

        blocked = False
        x = piece.x + delta_x
        y = piece.y + delta_y

        while 0 < x < 9 and 0 < y < 9 and not blocked and x != other_piece.x and y != other_piece.y:
            if self.is_exist(x, y):
                blocked = True
            else:
                x += delta_x
                y += delta_y
        return blocked

    def diff_color_point(self):
        """ calculate the point of the board with black and white pieces
        :return: total point
        """
        total = 0
        for piece in self.pieces:
            for other_piece in self.pieces:
                if piece != other_piece and piece.color != other_piece.color and piece.can_attack(
                        other_piece.x, other_piece.y) and not self.is_path_blocked(piece, other_piece):
                    total = total + 1

        return total

    # def print_board(self):
    #     """
    #     Print the current state of board with its pieces
    #     """
    #     board = [['.' for i in range(9)] for j in range(9)]

    #     for piece in self.pieces:
    #         if piece.piece_type == chesspiece.Chesspiece.knight:
    #             piece_type_char = 'K'
    #         elif piece.piece_type == chesspiece.Chesspiece.bishop:
    #             piece_type_char = 'B'
    #         elif piece.piece_type == chesspiece.Chesspiece.rook:
    #             piece_type_char = 'R'
    #         elif piece.piece_type == chesspiece.Chesspiece.queen:
    #             piece_type_char = 'Q'

    #         if piece.color == chesspiece.Chesspiece.black:
    #             piece_type_char = piece_type_char.lower()

    #         board[piece.x][piece.y] = piece_type_char

    #     for i in range(8, 0, -1):
    #         for j in range(1, 9):
    #             print(board[j][i], end=' ')
    #         print()
    #     print('\n', self.same_color_cost(), '\t', self.diff_color_point())

    
    def print_board(self):
        """Print board configuration along with it's cost and points."""
        piece_chars = {
            chesspiece.Chesspiece.black: {
                chesspiece.Chesspiece.bishop: '\u2657',
                chesspiece.Chesspiece.rook: '\u2656',
                chesspiece.Chesspiece.queen: '\u2655',
                chesspiece.Chesspiece.knight: '\u2658',
            },
            chesspiece.Chesspiece.white: {
                chesspiece.Chesspiece.bishop: '\u265d',
                chesspiece.Chesspiece.rook: '\u265c',
                chesspiece.Chesspiece.queen: '\u265b',
                chesspiece.Chesspiece.knight: '\u265e',
            }
        }

        board = [['.' for i in range(9)] for j in range(9)]

        for piece in self.pieces:
            board[piece.x][piece.y] = piece_chars[piece.color][piece.piece_type]
        for i in range(8, 0, -1):
            for j in range(1, 9):
                print(board[j][i], end=' ')
            print()
        print('\n', self.same_color_cost(), '\t', self.diff_color_point())