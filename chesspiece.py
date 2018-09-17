# chesspiece berisi kelas Chesspiece

# Kelas Chesspiece merepresentasikan sebuah bidak dalam papan catur


class Chesspiece:
    # Konstanta-konstanta yang digunakan pada kelas Chesspiece
    knight = 1
    bishop = 2
    rook = 3
    queen = 4
    black = 0
    white = 1

    # Konstruktor Chesspiece melakukan assignment nilai-nilai dasar dari piece
    def __init__(self, piece_type, color, x, y):
        self.piece_type = piece_type
        self.color = color
        self.x = x
        self.y = y
        self.movement = []

    # Operator assignment untuk Chesspiece
    def __eq__(self, other):
        if self.piece_type == other.piece_type and self.color == other.color and self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    # can_attack mengembalikan nilai True jika Chesspiece dapat
    # menyerang Chesspiece lain pada posisi (x,y)
    def can_attack(self, x, y):
        if self.piece_type == self.queen:
            return self.can_attack_queen(x, y)
        elif self.piece_type == self.rook:
            return self.can_attack_rook(x, y)
        elif self.piece_type == self.bishop:
            return self.can_attack_bishop(x, y)
        elif self.piece_type == self.knight:
            return self.can_attack_knight(x, y)
        return False

    def can_attack_queen(self, x, y):
        if self.x == x or self.y == y or abs(self.x-x) == abs(self.y-y):
            return True
        return False

    def can_attack_rook(self, x, y):
        if self.x == x or self.y == y:
            return True
        return False

    def can_attack_knight(self, x, y):
        if self.x + 2 == x and self.y+1 == y and self.x + 2 <= 8 and self.y + 1 <= 8:
            return True
        elif self.x - 2 == x and self.y+1 == y and self.x - 2 >= 1 and self.y + 1 <= 8:
            return True
        elif self.x + 2 == x and self.y-1 == y and self.x + 2 <= 8 and self.y - 1 >= 1:
            return True
        elif self.x - 2 == x and self.y-1 == y and self.x - 2 >= 1 and self.y - 1 >= 1:
            return True
        elif self.y + 2 == y and self.x-1 == x and self.x - 1 >= 1 and self.y + 2 <= 8:
            return True
        elif self.y - 2 == y and self.x-1 == x and self.x - 1 >= 1 and self.y - 2 >= 1:
            return True
        elif self.y + 2 == y and self.x+1 == x and self.x + 1 <= 8 and self.y + 2 <= 8:
            return True
        elif self.y - 2 == y and self.x+1 == x and self.x + 1 <= 8 and self.y - 2 >= 1:
            return True

        return False

    def can_attack_bishop(self, x, y):
        if abs(self.x-x) == abs(self.y-y):
            return True
        return False
