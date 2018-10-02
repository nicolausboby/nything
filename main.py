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


import Hill
import genetic
import annealing
from board import Board

# Program utama akan dimulai dengan membuat sebuah objek board
# kemudian memanggil ketiga fungsi local search yang telah dibuat
if __name__ == "__main__":

    choice = 0

    mboard = Board()

    print('========================================')
    print('TUGAS BESAR 1 IF3170 INTELEGENSI BUATAN')
    print()
    print('N-YTHING PROBLEM')
    print('========================================')
    print('Kelompok 1 :')
    print('Ferdiant Joshua M. - 13516047')
    print('Nicolaus Boby A.   - 13516077')
    print('Christian Jonathan - 13516092')
    print('Christian Jonathan - 13516092')
    print('Cornelius Yan M.   - 13516113')
    print('----------------------------------------\n')
    while choice != 4:
        print('1. Stochastic Hill Climbing')
        print('2. Simulated Annealing')
        print('3. Genetic Algorithm')
        print('4. Exit')
        choice = int(input('Choose an algorithm : '))

        if choice == 1:
            Hill.solve_hill(mboard)
        elif choice == 2:
            annealing.solve_annealing(mboard)
        elif choice == 3:
            genetic.solve_genetic(mboard)
        elif choice == 4:
            print('Have a nice day!\n')
        else:
            print('\nInvalid choice! Choose between 1-4\n')