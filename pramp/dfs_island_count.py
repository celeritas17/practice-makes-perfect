def get_neighbors(row, col, num_rows, num_cols):
	neighbors = []
	if row > 0:
		neighbors.append((row - 1, col))
	if row < num_rows:
		neighbors.append((row + 1, col))
	if col > 0:
		neighbors.append((row, col - 1))
	if col < num_cols:
		neighbors.append((row, col + 1))

	return neighbors


def DFS(row, col, matrix, explored):
	explored[row][col] = True
	for neighbor in get_neighbors(row, col, len(matrix) - 1, len(matrix[0]) - 1):
		neighbor_row, neighbor_col = neighbor
		if matrix[neighbor_row][neighbor_col] == 1 and not explored[neighbor_row][neighbor_col]:
			DFS(neighbor_row, neighbor_col, matrix, explored) 

def dfs_loop(matrix):
	island_count = 0
	explored = []
	for i in range(len(matrix)):
		explored.append([False]*len(matrix[0]))

	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 1 and not explored[row][col]:
				island_count += 1
				DFS(row, col, matrix, explored)

	return island_count

if __name__ == '__main__':
	matrix = [
		[0, 1, 0, 1, 0],
		[0, 0, 1, 1, 1],
		[1, 0, 0, 1, 1],
		[0, 1, 1, 0, 0],
		[1, 0, 1, 0, 1]
	]
	print(dfs_loop(matrix))
	