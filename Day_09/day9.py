def print_2D(double_array):
	for row in double_array:
		print(row)

def load_data(filename):
	"""
	Loads data as 2d int array
	"""
	file = open(filename, 'r')
	data = file.read().splitlines()
	for index, line in enumerate(data):
		data[index] = list(line)
		data[index] = [int(x) for x in data[index]]
	return data

def add_borders(grid):
	""" Add a 10 around the whole grid """
	grid_height = len(grid)
	n = len(grid[0]) + 2
	top_bottom = [10] * n
	for i in range(grid_height):
		grid[i].insert(0, 10)
		grid[i].append(10)
	grid.insert(0,top_bottom)
	grid.append(top_bottom)
	return grid

def lowpoint_score(grid):
	""" Find low points """
	total_res = 0
	grid_height = len(grid) - 1
	grid_width = len(grid[0]) - 1
	for i_row in range(1, grid_height):
		for i_num in range(1, grid_width):
			middle = grid[i_row][i_num]
			left = grid[i_row][i_num - 1]
			right = grid[i_row][i_num + 1]
			down = grid[i_row + 1][i_num]
			up = grid[i_row - 1][i_num]
			# print(f"\n  {up}  ")
			# print(f"{left} {middle} {right}")
			# print(f"  {down}  ")
			if middle<left and middle<right and middle<up and middle<down and middle<up and middle<down:
				total_res += middle + 1
	return total_res

if __name__ == "__main__":
	vents = load_data("input.txt")
	add_borders(vents)
	score = lowpoint_score(vents)
	# print_2D(vents)
	print("score: ", score)
