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
		while step < limit and best_cost > 0:
			t = tmax * np.exp(r * step / limit)

			# making sure that t is a feasible temperature parameter, above zero
			# and finding all of the possible movement of a random chess piece
			if t <= 0:
				break
			step += 1
			ccost = board.calculate_cost()
			all_pieces = board.pieces
			select_piece = all_pieces[random.randint(0, len(all_pieces) - 1)]
			allmove = find_movement(select_piece, board)

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
		if current_result['best_cost'] == 0:
			success += 1
		best_result = get_best_result(current_result)
		print(str(round((current_result['total_time'] * 1000), 4)) + ' ms' + ', cost =' + str(
			current_result['best_cost']))
	success_stat = round((success / int(input_runs)), 4)

	# Output section
	#
	print('\n')
	best_result['board'].print_board()
	print('\n\n================================================================')
	print('\n-----------------SIMULATED ANNEALING ALGORITHM------------------\n')
	print('Total run(s):     {}'.format(input_runs))
	print('Solution found:   {} times, with statistic {} %'.format(success, success_stat * 100))
	print('\nBEST RESULT:')
	print('  > final cost:   {}'.format(best_result['final_cost']))
	print('  > best cost:    {}'.format(best_result['best_cost']))
	print('  > total step:   {}'.format(best_result['step']))
	print('  > improved:     {}'.format(best_result['improve']))
	print('  > accepted:     {}'.format(best_result['accept']))
	print('  > elapsed time: {} ms'.format(best_result['total_time'] * 1000))
	print('\n================================================================\n')


def find_movement(piece, board):
	""" finds all of the possible movement of a input chess piece ont the board

	:param piece: selected chess piece
	:param board: current state of the board

	:return: movement -> a list of possible moves
	"""
	movement = []

	def find_horizontal(piece, board):
		found_right = False
		found_left = False
		x = piece.x - 1
		y = piece.y
		hmove = []
		while x > 0 and not found_left:
			if board.is_exist(x, y):
				found_left = True
			else:
				hmove.append([x, y])
				x -= 1

		x = piece.x + 1
		while x < 9 and not found_right:
			if board.is_exist(x, y):
				found_right = True
			else:
				hmove.append([x, y])
				x += 1
		return hmove

	def find_vertical(piece, board):
		found_up = False
		found_down = False
		x = piece.x
		y = piece.y - 1
		vmove = []
		while y > 0 and not found_down:
			if board.is_exist(x, y):
				found_down = True
			else:
				vmove.append([x, y])
				y -= 1

		y = piece.y + 1
		while y < 9 and not found_up:
			if board.is_exist(x, y):
				found_up = True
			else:
				vmove.append([x, y])
				y += 1
		return vmove

	def find_diagonal(piece, board):
		found_up_left = False
		found_up_right = False
		found_down_left = False
		found_down_right = False
		x = piece.x - 1
		y = piece.y - 1
		dmove = []
		while x > 0 and y > 0 and not found_down_left:
			if board.is_exist(x, y):
				found_down_left = True
			else:
				dmove.append([x, y])
				x -= 1
				y -= 1

		x = piece.x - 1
		y = piece.y + 1
		while x > 0 and y < 9 and not found_up_left:
			if board.is_exist(x, y):
				found_up_left = True
			else:
				dmove.append([x, y])
				x -= 1
				y += 1

		x = piece.x + 1
		y = piece.y + 1
		while x < 9 and y < 9 and not found_up_right:
			if board.is_exist(x, y):
				found_up_right = True
			else:
				dmove.append([x, y])
				x += 1
				y += 1

		x = piece.x + 1
		y = piece.y - 1
		while x < 9 and y > 0 and not found_down_right:
			if board.is_exist(x, y):
				found_down_right = True
			else:
				dmove.append([x, y])
				x += 1
				y -= 1
		return dmove

	def knight_move(piece, board):
		kmove = []
		for x in range(0, 9):
			for y in range(0, 9):
				if piece.can_attack_knight(x, y) and not board.is_exist(x, y):
					kmove.append([x, y])
		return kmove

	if piece.piece_type == chesspiece.Chesspiece.queen:
		movement.extend(find_horizontal(piece, board))
		movement.extend(find_vertical(piece, board))
		movement.extend(find_diagonal(piece, board))
	elif piece.piece_type == chesspiece.Chesspiece.rook:
		movement.extend(find_horizontal(piece, board))
		movement.extend(find_vertical(piece, board))
	elif piece.piece_type == chesspiece.Chesspiece.bishop:
		movement.extend(find_diagonal(piece, board))
	elif piece.piece_type == chesspiece.Chesspiece.knight:
		movement.extend(knight_move(piece, board))

	return movement
