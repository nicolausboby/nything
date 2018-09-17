# Tugas Besar IF3170 Inteligensi Buatan
# N-ything problem
#
# Oleh Kelompok 1 - FIRST
# Anggota :
# Ferdiant Joshua M. - 13516047
# Nicolaus Boby A.   - 13516077
# Christian Jonathan - 13516092
# Faza Fahleraz      - 13516096
# Cornelius Yan M.   - 13516113


import hill
import genetic
import annealing
from board import Board

# Program utama akan dimulai dengan membuat sebuah objek board
# kemudian memanggil ketiga fungsi local search yang telah dibuat
if __name__ == "__main__":

    mboard = Board()

    hill.solve_hill(mboard)
    annealing.solve_annealing(mboard)
    genetic.solve_genetic(mboard)