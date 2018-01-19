from piece import *

class Board:
    def __init__(self, files=8, ranks=8):
        self.files = files
        self.ranks = ranks
        self.board_arr = [[None for i in range(self.ranks)] for j in range(self.files)]

        self.setup_board_normal()

    def ascii(self):
        """ Print current board state in ascii format"""
        for r in reversed(range(self.ranks)): # Go through each row
            row = ""
            for f in range(self.files):
                if self.board_arr[r][f] is None:
                    row = row + " . "
                else:
                    row = row + " " + str(self.board_arr[r][f]) + " "
            print(row)

    def setup_board_normal(self):
        # Back ranks
        for row, color in zip([0,7], Colors):
            self.board_arr[row][0] = Rook(color)
            self.board_arr[row][1] = Knight(color)
            self.board_arr[row][2] = Bishop(color)
            self.board_arr[row][3] = Queen(color)
            self.board_arr[row][4] = King(color)
            self.board_arr[row][5] = Bishop(color)
            self.board_arr[row][6] = Knight(color)
            self.board_arr[row][7] = Rook(color)

        # Pawns
        for row, color in zip([1,6], Colors):
            for f in range(self.files):
                self.board_arr[row][f] = Pawn(color)

if __name__ == "__main__":
    board = Board()
    board.ascii()
