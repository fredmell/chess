import utils

from piece import *

class Board:
    def __init__(self, files=8, ranks=8):
        self.files = files
        self.ranks = ranks
        self.board_arr = [[None for i in range(self.ranks)] for j in range(self.files)]
        self.taken = [] # All eliminated pieces

    def at(self, fil, rank):
        return self.board_arr[rank][fil]

    def is_empty(self, fil, rank):
        return self.at(fil, rank) == "."

    def print_ascii(self, key=True):
        """ Print current board state in ascii format"""
        full_string = "\n"
        for r in reversed(range(self.ranks)): # Go through each row
            row = ""
            if key:
                row += "{}  ".format(r+1)
            for f in range(self.files):
                row = row + " " + str(self.board_arr[r][f]) + " "
            full_string += row + "\n"
        if key:
            full_string += "    A  B  C  D  E  F  G  H\n"
        return full_string.rstrip()

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

        # Empty fields
        for i in range(self.files):
            for j in range(self.ranks):
                if self.board_arr[i][j] is None:
                    self.board_arr[i][j] = Empty()

    def move(self, frm, to):
        frm_txt = frm
        frm = utils.let_to_coords(frm)
        to = utils.let_to_coords(to)

        if self.is_empty(*frm):
            print("No piece at {}. Unable to move.".format(frm_txt))
            return

        else:
            self.board_arr[to[1]][to[0]] = self.board_arr[frm[1]][frm[0]]
            self.board_arr[frm[1]][frm[0]] = Empty()

if __name__ == "__main__":
    board = Board()
    board.setup_board_normal()
    print(board.print_ascii())
    board.move("e2", "e4")
    print(board.print_ascii())
