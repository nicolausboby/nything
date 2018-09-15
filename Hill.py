# FIRST project
# For solving N-ything problem, a modified version of N-Queens problem
# Hill Climbing Algorithm

import board
import time
import random
import copy
import chesspiece
from annealing import find_movement


def solve_hill(board):
	best_cost = 9999
	ccost = 0
	input_limit = input('enter iteration limit :')
	print('limit = ' + str(input_limit))
	limit = int(input_limit)
	start = time.time()
	step = improve = 0
	while step < limit and best_cost > 0:
		step += 1
		ccost = board.calculate_cost()
		all_pieces = board.pieces
		select_piece = all_pieces[random.randint(0, len(all_pieces) - 1)]
		allmove = find_movement(select_piece, board)
		while len(allmove) > 0:
			temp_board = copy.deepcopy(board)
			select_move = allmove[random.randint(0, len(allmove) - 1)]
			allmove.remove(select_move)
			temp_board.pieces.remove(select_piece)
			temp_board.pieces.append(
				chesspiece.Chesspiece(select_piece.piece_type, select_piece.color, select_move[0], select_move[1]))
			next_cost = temp_board.calculate_cost()
			dE = next_cost - ccost
			if dE < 0.0:
				board = temp_board
				ccost = next_cost
				improve += 1
			# print('IMPROVED!')
			if next_cost < best_cost:
				best_cost = next_cost
			break
	board.print_board()
	print('\n\n================================================================')
	print('\n--------------------HILL CLIMBING ALGORITHM---------------------\n')
	print('final cost	= {}'.format(ccost))
	print('best cost	= {}'.format(best_cost))
	print('step 		= {}'.format(step))
	print('improved	= {}'.format(improve))
	print('elapsed time	= {} ms'.format((time.time() - start) * 1000))
	print('\n\n')
