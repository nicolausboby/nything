# Chessboard containing 

file_input = 'input.txt'

class Board:
	def __init__(self):
		with open(file_input, 'rt') as f_in:
			current_list = []
			lines = f_in.readlines()
			for line in lines:
				clear = line.replace('\n','')
				current_list.append(line.split())
		
		return self

