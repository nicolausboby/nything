# FIRST project
# N-ything problem, a modified version of the famous N-queens Problem in AI

import hill
import genetic
import annealing
from board import Board


if __name__ == "__main__":

    mboard = Board()

    hill.solve_hill(mboard)
    annealing.solve_annealing(mboard)
    genetic.solve_genetic(mboard)