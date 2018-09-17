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
	input_runs = input('enter amount of trial: ')
	print('trial run(s) = ' + str(input_runs))
	input_limit = input('enter iteration limit: ')
	print('limit = ' + str(input_limit) + '\n')
	limit = int(input_limit)
	best_result = {}
	success = 0

	def get_best_result(new_result):
		if len(best_result) == 0:
			return new_result
		elif best_result['best_cost'] > new_result['best_cost']:
			return new_result
		return best_result

	def solver(board, limit):
		best_cost = 9999
		ccost = 0
		step = improve = 0
		end_time = start_time = time.time()
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
		end_time = time.time()
		total_time = end_time - start_time
		result = {
			"best_cost": best_cost,
			"final_cost": ccost,
			"total_time": total_time,
			"improve": improve,
			"step": step,
			"board": board
		}
		return result

	for i in range(int(input_runs)):
		board.randomize_pieces()
		current_result = solver(board, limit)
		if current_result['best_cost'] == 0:
			success += 1
		best_result = get_best_result(current_result)
		print(str(round((current_result['total_time'] * 1000), 4)) + ' ms' + ', cost =' + str(current_result['best_cost']))
	success_stat = round((success / int(input_runs)), 4)

	print('\n')
	best_result['board'].print_board()
	print('\n\n================================================================')
	print('\n------------------- HILL CLIMBING ALGORITHM -------------------\n')
	print('Total run(s):     {}'.format(input_runs))
	print('Solution found:   {} times, with statistic {} %'.format(success, success_stat * 100))
	print('\nBEST RESULT:')
	print('  > final cost:   {}'.format(best_result['final_cost']))
	print('  > best cost:    {}'.format(best_result['best_cost']))
	print('  > total step:   {}'.format(best_result['step']))
	print('  > improved:     {}'.format(best_result['improve']))
	print('  > elapsed time: {} ms'.format(best_result['total_time'] * 1000))
	print('\n================================================================\n')
