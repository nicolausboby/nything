# FIRST project
# N-ything problem, a modified version of the famous N-queens Problem in AI

import hill
import genetic
import annealing
import board as b


file_input = "input.txt"
piecelist = []

def readFile():
	with open(file_input, 'rt') as f_in:
		current_list = []
		lines = f_in.readlines()
		for line in lines:
			clear = line.replace('\n','')
			current_list.append(line.split())
	return current_list
	

if __name__ == "__main__":
	piecelist = readFile()
	mboard = b.Board()
	for i in range(0,8):
		for j in range(0,8):
			print(mboard.ChessBoard[i][j],end=' ')
		print()

	hill.solve_hill(mboard)
	annealing.solve_annealing(mboard)
	genetic.solve_genetic(mboard)


