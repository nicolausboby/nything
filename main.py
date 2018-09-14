# FIRST project
# N-ything problem, a modified version of the famous N-queens Problem in AI

import Hill
import genetic
import annealing
from board import Board


file_input = "input.txt"
piecelist = []


if __name__ == "__main__":

    mboard = Board()
    mboard.print_board()

    Hill.solve_hill(mboard)
    annealing.solve_annealing(mboard)
    genetic.solve_genetic(mboard)
