# FIRST project
# N-ything problem, a modified version of the famous N-queens Problem in AI

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
	print(piecelist)
