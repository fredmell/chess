import abc
import enum

class Colors(enum.Enum):
    WHITE = 1
    BLACK = 2

class Piece(abc.ABC):
    def __init__(self, color=None):
        self.color = color
        self.symbol = None

    def __str__(self):
        if self.symbol == ".":
            return self.symbol

        if self.color == Colors.WHITE:
            return self.symbol

        elif self.color == Colors.BLACK:
            return self.symbol.capitalize()

        else:
            raise TypeError("Piece does not have a color.")

    def set_color(color):
        self.color = color

class Empty(Piece):
    def __init__(self):
        self.color = None
        self.symbol = '.'

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'k'

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'q'

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'b'

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'n'

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'p'

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'r'
