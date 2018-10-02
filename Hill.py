# FIRST project
# For solving N-ything problem, a modified version of N-Queens problem
# Hill Climbing Algorithm

import time
from copy import deepcopy
import chesspiece


def solve_hill(board):
	""" main function for the Hill Climbing algorithm for N-ything problem

	:param board: Inisial state of the board

	# I.S : unsolved board
	# F.S : solved board (global or local maximum)
	Solution is printed out
	"""
	print('\nStochastic Hill Climbing')
	print('----------------------------------------')
	input_runs = input('Enter amount of trial: ')
	print('Trial run(s) = ' + str(input_runs))
	input_limit = input('Enter iteration limit: ')
	print('Limit = ' + str(input_limit) + '\n')
	limit = int(input_limit)
	best_result = {}
	total_time = 0
	success = 0

	def get_best_result(new_result):
		""" update the value of best result

		:param new_result: a new result
		:return: (best_result) : compared best result
		"""
		if len(best_result) == 0:
			return new_result
		elif best_result['best_cost'] > new_result['best_cost']:
			return new_result
		elif best_result['best_cost'] == new_result['best_cost']:
			if best_result['total_time'] > new_result['total_time']:
				return new_result
		return best_result

	def solver(board, limit):
		""" function to solve a simulated algorithm once, iteration limited

		:param board: Inisial state of the board
		:param limit: iteration limit
		:return: Solution board, costs, time
		"""
		best_cost = 9999
		ccost = 0
		step = improve = 0
		start_time = time.time()
		peak = False
		while step < limit and not peak:
			ccost = board.calculate_cost()
			all_pieces = deepcopy(board.pieces)
			proceed = True
			while len(all_pieces) > 0 and proceed:
				select_piece = all_pieces[0]
				all_possible_move = []
				for i in range(1, 9):
					for j in range(1, 9):
						if not board.is_exist(i, j):
							all_possible_move.append([i, j])

				all_move_cost = {}

				# find all of the possible cost
				for move in all_possible_move:
					temp_board = deepcopy(board)
					temp_board.pieces.remove(select_piece)
					temp_board.pieces.append(
						chesspiece.Chesspiece(select_piece.piece_type, select_piece.color, move[0], move[1]))
					all_move_cost.update({(move[0], move[1]): temp_board.calculate_cost()})
					del temp_board

				# for each move in all move cost, if there is a better move, move the piece
				while len(all_move_cost) > 0:
					# print(all_move_cost)
					local_best_move = min(all_move_cost.items(), key=lambda x: x[1])
					# print(local_best_move)
					next_cost = local_best_move[1]
					temp_board = deepcopy(board)
					new_x = local_best_move[0][0]
					new_y = local_best_move[0][1]
					temp_board.pieces.remove(select_piece)
					temp_board.pieces.append(
						chesspiece.Chesspiece(select_piece.piece_type, select_piece.color, new_x, new_y))
					if next_cost < ccost:
						board = temp_board
						ccost = next_cost
						improve += 1
						step += 1
						proceed = False
						if next_cost < best_cost:
							best_cost = next_cost
						break
					else:  # if the next cost > ccost
						all_move_cost.pop(local_best_move[0])
						# print(all_move_cost)
						if len(all_move_cost) <= 0:
							all_pieces.remove(select_piece)
							if len(all_pieces) <= 0:
								peak = True
								proceed = False
							break

		end_time = time.time()
		total_time = end_time - start_time
		result = {
			"best_cost": best_cost,
			"total_time": total_time,
			"improve": improve,
			"step": step,
			"board": board
		}
		return result

	# continuation of the main function
	# running trials run, and searching for the best result
	for i in range(int(input_runs)):
		board.randomize_pieces()
		current_result = solver(board, limit)
		total_time += current_result['total_time']
		if current_result['best_cost'] == 0:
			success += 1
		best_result = get_best_result(current_result)
		print('{} ms, cost = {}, step = {}'. \
			format(round((current_result['total_time'] * 1000), 4), current_result['best_cost'], current_result['step']))
	success_stat = round((success / int(input_runs)), 4)

	# Output section
	#
	print('\n')
	print('\n\n================================================================')
	print('\n------------------- HILL CLIMBING ALGORITHM -------------------\n')
	print('Total run(s):	{}'.format(input_runs))
	print('Elapsed time:	{} ms'.format(round(total_time*1000, 3)))
	print('\nBEST RESULT:')
	print('  > best cost    :{}'.format(best_result['best_cost']))
	print('  > total step   :{}'.format(best_result['step']))
	print('  > running time: {} ms\n'.format(round(best_result['total_time'] * 1000, 3)))
	best_result['board'].print_board()
	print('\n================================================================\n')
