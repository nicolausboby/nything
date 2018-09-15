# FIRST project
# Simulated annealing algorithm

import board
import chesspiece
import numpy as np
import random
import copy
import time


def solve_annealing(board):
	best_cost = 0
	input_limit = input('enter iteration limit :')
	print('limit = ' + str(input_limit))
	limit = int(input_limit)
	tmax = 10000
	tmin = 0.1
	r = -np.log(tmax/tmin)
	start = time.time()
	step = improve = accept = 0
	while step < limit:
		t = tmax * np.exp(r*step/limit)
		if t <= 0:
			break
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
				chesspiece.Chesspiece(select_piece.pieceType, select_piece.color, select_move[0], select_move[1]))
			next_cost = temp_board.calculate_cost()
			dE = next_cost - ccost
			# print('current cost	= {}'.format(ccost))
			# print('next cost	= {}'.format(next_cost))
			# print('t		= {}'.format(t))
			# print(np.exp(-dE / t))
			random_chance = random.random()
			if dE > 0.0 and np.exp(-dE / t) > random_chance:
				board = temp_board
				ccost = next_cost
				accept += 1
				# print('ACCEPTED with random chance = {}'.format(random_chance))
				break
			else:  # dE < 0, next_cost < ccost
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
	print('final cost	= {}'.format(ccost))
	print('step 		= {}'.format(step))
	print('improve		= {}'.format(step))
	# print('accept 	= {}'.format(accept))
	print('best cost	= {}'.format(best_cost))
	print('elapsed time	= {} ms'.format((time.time() - start) * 1000))


def descent_function(func, t, rate):
	if func == "LINEAR":
		return t - rate
	elif func == "LOG":
		return t * rate
	elif func == "CONSTANT":
		return t


def find_movement(piece, board):
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

	if piece.pieceType == chesspiece.Chesspiece.queen:
		movement.extend(find_horizontal(piece, board))
		movement.extend(find_vertical(piece, board))
		movement.extend(find_diagonal(piece, board))
	elif piece.pieceType == chesspiece.Chesspiece.rook:
		movement.extend(find_horizontal(piece, board))
		movement.extend(find_vertical(piece, board))
	elif piece.pieceType == chesspiece.Chesspiece.bishop:
		movement.extend(find_diagonal(piece, board))
	elif piece.pieceType == chesspiece.Chesspiece.knight:
		movement.extend(knight_move(piece, board))

	return movement
