# TODO: Tambah keterangan file ini


class Chesspiece:
    knight = 1
    bishop = 2
    rook = 3
    queen = 4
    black = 0
    white = 1

    def __init__(self, piece_type, color, x, y):
        self.pieceType = piece_type
        self.color = color
        self.x = x
        self.y = y
        self.movement = []

    def can_attack(self, x, y):
        if self.pieceType == self.queen:
            return self.can_attack_queen(x, y)
        elif self.pieceType == self.rook:
            return self.can_attack_rook(x, y)
        elif self.pieceType == self.bishop:
            return self.can_attack_bishop(x, y)
        elif self.pieceType == self.knight:
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
