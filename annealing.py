# FIRST project
# Simulated annealing algorithm

import chesspiece
import numpy as np
import random
import copy
import time


def solve_annealing(board):
	""" main function for the Simulated Annealing algorithm for N-ything problem

	:param board: Inisial state of the board

	# I.S : unsolved board
	# F.S : solved board (global or local maximum)
	Solution printed out
	"""
	# initialisation and read input parameters
	input_runs = input('enter amount of trial: ')
	print('trial run(s) = ' + str(input_runs))
	input_limit = input('enter iteration limit: ')
	print('limit = ' + str(input_limit) + '\n')
	limit = int(input_limit)
	best_result = {}
	success = 0
	total_time = 0

	def solver(board, limit):
		""" function to solve a simulated algorithm once, iteration limited

		:param board: Inisial state of the board
		:param limit: iteration limit
		:return: Solution board, costs, time, and statistics
		"""
		best_cost = 9999
		ccost = 0
		tmax = 1000
		tmin = 0.1
		r = -np.log(tmax / tmin)
		start_time = time.time()
		step = improve = accept = 0

		# loop the process of each iteration
		# the loop will stop if the limit step has been reached, or solution has been found
		while step < limit :
			t = tmax * np.exp(r * step / limit)

			# making sure that t is a feasible temperature parameter, above zero
			# and finding all of the possible movement of a random chess piece
			if t <= 0:
				break
			step += 1
			ccost = board.calculate_cost()
			all_pieces = board.pieces
			select_piece = all_pieces[random.randint(0, len(all_pieces) - 1)]
			allmove = []
			for i in range(1, 9):
				for j in range(1, 9):
					if not board.is_exist(i, j):
						allmove.append([i, j])

			# checking a random move of the previously selected piece
			# if the move has better 'energy' select it,
			# if it is not, with a probability from a distribution might be selected
			while len(allmove) > 0:
				temp_board = copy.deepcopy(board)
				select_move = allmove[random.randint(0, len(allmove) - 1)]
				allmove.remove(select_move)
				temp_board.pieces.remove(select_piece)
				temp_board.pieces.append(
					chesspiece.Chesspiece(select_piece.piece_type, select_piece.color, select_move[0], select_move[1]))
				next_cost = temp_board.calculate_cost()
				dE = next_cost - ccost
				random_chance = random.random()

				# evaluating Boltzmann's Distribution
				if dE > 0.0 and np.exp(-dE / t) > random_chance:
					board = temp_board
					ccost = next_cost
					accept += 1
					break
				else:  # dE < 0, next_cost < ccost
					if dE < 0.0:
						board = temp_board
						ccost = next_cost
						improve += 1
					if next_cost < best_cost:
						best_cost = next_cost
					break

		# returning the result and time spent
		end_time = time.time()
		total_time = end_time - start_time
		result = {
			"best_cost": best_cost,
			"final_cost": ccost,
			"total_time": total_time,
			"improve": improve,
			"accept": accept,
			"step": step,
			"board": board
		}
		return result

	def get_best_result(new_result):
		""" update the value of best result

		:param new_result: a new result
		:return: (best_result) : compared best result
		"""
		if len(best_result) == 0:
			return new_result
		elif best_result['best_cost'] > new_result['best_cost']:
			return new_result
		return best_result

	# continuation of the main function
	# running trials run, and searching for the best result
	for i in range(int(input_runs)):
		board.randomize_pieces()
		current_result = solver(board, limit)
		total_time += current_result['total_time']
		if current_result['best_cost'] == 0:
			success += 1
		best_result = get_best_result(current_result)
		print(str(round((current_result['total_time'] * 1000), 4)) + ' ms' + ', cost =' + str(
			current_result['best_cost']))
	success_stat = round((success / int(input_runs)), 4)

	# Output section
	#
	print('\n')
	print('\n\n================================================================')
	print('\n-----------------SIMULATED ANNEALING ALGORITHM------------------\n')
	print('Total run(s):     {}'.format(input_runs))
	print('Elapsed time:	{} ms'.format(round(total_time * 1000, 3)))
	print('\nBEST RESULT:')
	print('  > final cost:   {}'.format(best_result['final_cost']))
	print('  > best cost:    {}'.format(best_result['best_cost']))
	print('  > total step:   {}'.format(best_result['step']))
	print('  > improved:     {}'.format(best_result['improve']))
	print('  > accepted:     {}'.format(best_result['accept']))
	print('  > running time: {} ms\n'.format(best_result['total_time'] * 1000))
	best_result['board'].print_board()
	print('\n================================================================\n')
