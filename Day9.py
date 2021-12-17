#Day9.py
import numpy as np

def create_matrix():
	with open('input_9.txt') as file:
		line = file.readline()
		matrix = np.array(list(map(int, list(line.rstrip()))))
		
		for line in file.readlines():
			arr = np.array(list(map(int, list(line.rstrip()))))
			matrix = np.vstack([matrix, arr])

	return matrix
	
def is_smallest(matrix, pos):
	is_smallest = True
	neighbor_positions = np.array(((1, 0), (-1, 0), (0, 1), (0, -1)))
	for neighbor_pos in neighbor_positions:
		try:
			neighbor = matrix[tuple(np.array(pos)+neighbor_pos)]
		except IndexError:
			pass
		else:
			if neighbor <= matrix[pos]:
				is_smallest = False
	return is_smallest

def eval_risk(matrix):
	risk = 0
	marked_matrix = matrix.copy()
	rows, cols = matrix.shape
	for row in range(rows):
		for col in range(cols):
			pos = row, col
			if is_smallest(matrix, pos):
				marked_matrix[pos] = int('1'+str(matrix[pos]))
				risk += matrix[pos]+1
	
	return risk, marked_matrix
	
def main():
	matrix = create_matrix()
	risk, marked_matrix = eval_risk(matrix)
	
	print(marked_matrix)
	print(risk)
	
if __name__ == '__main__':
	main()
	

				
	
