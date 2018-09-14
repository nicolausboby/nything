

class Chesspiece:
    knight = 1
    bishop = 2
    rook = 3
    queen = 4

    def __init__(self, pieceType, color, x, y):
        self.pieceType = pieceType
        self.color = color
        self.x = x
        self.y = y
        self.movement = []

    def canAttack(x, y):
        if self.pieceType == queen:
            return self.canAttackQueen(x, y)
        return false

    def canAttackQueen(x, y):
        if self.x != x and self.y != y and self.x - self.y != x-y and self.y - self.x != y-x:
            return false
        return true

    def canAttackRook(x, y):
        if self.x != x and self.y != y:
            return false
        return true

    def canAttackKnight(x, y):
        if self.x + 2 == x and self.y+1 == y and self.x + 2 <= 8 and self.y + 1 <= 8:
            return true
        elif self.x - 2 == x and self.y+1 == y and self.x - 2 >= 1 and self.y + 1 <= 8:
            return true
        elif self.x + 2 == x and self.y-1 == y and self.x + 2 <= 8 and self.y - 1 >= 1:
            return true
        elif self.x - 2 == x and self.y-1 == y and self.x - 2 >= 1 and self.y - 1 >= 1:
            return true
        elif self.y + 2 == x and self.x-1 == y and self.x - 1 >= 1 and self.y + 2 <= 8:
            return true
        elif self.y - 2 == x and self.x-1 == y and self.x - 1 >= 1 and self.y - 2 >= 1:
            return
        elif self.y + 2 == x and self.x+1 == y and self.x + 1 <= 8 and self.y + 2 <= 8:
            return true
        elif self.y - 2 == x and self.x+1 == y and self.x + 1 <= 8 and self.y - 2 >= 1:
            return true

        return false

    def canAttackBishop(x, y):
        if self.x - self.y != x-y and self.y - self.x != y-x:
            return false
        return true
