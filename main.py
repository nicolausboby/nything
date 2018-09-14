# FIRST project
# N-ything problem, a modified version of the famous N-queens Problem in AI

import Hill
import genetic
import annealing
import board


file_input = "input.txt"
piecelist = []


if __name__ == "__main__":

    mboard = board.Board
    print(mboard)

    for i in range(0, 8):
        for j in range(0, 8):
            print(".", end=' ')
        print()

    Hill.solve_hill(mboard)
    annealing.solve_annealing(mboard)
    genetic.solve_genetic(mboard)
