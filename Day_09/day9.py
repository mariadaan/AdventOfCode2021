import math

def print_2D(double_array):
	""" Print 2D array """
	for row in double_array:
		print(row)

def load_data(filename):
	""" Loads data as 2d int array """
	file = open(filename, 'r')
	data = file.read().splitlines()
	for index, line in enumerate(data):
		data[index] = list(line)
		data[index] = [int(x) for x in data[index]]
	return data

def add_borders(grid, pad):
	""" Add a padding around the whole grid """
	grid
	grid_height = len(grid)
	n = len(grid[0]) + 2
	top_bottom = [pad] * n
	for i in range(grid_height):
		grid[i].insert(0, pad)
		grid[i].append(pad)
	grid.insert(0,top_bottom)
	grid.append(top_bottom)
	return grid

def get_basin_size(grid, x, y, size = 0):
	""" Get the size of a basin """
	grid[y][x] = 9
	if grid[y][x - 1] != 9:
		size += get_basin_size(grid, x - 1, y)
	if grid[y][x + 1] != 9:
		size += get_basin_size(grid, x + 1, y)
	if grid[y + 1][x] != 9:
		size += get_basin_size(grid, x, y + 1)
	if grid[y - 1][x] != 9:
		size += get_basin_size(grid, x, y - 1)
	return size + 1

def find_basins(grid):
	""" Calculate sum of low points and basin sizes"""
	sizes = []
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
			if middle<left and middle<right and middle<up and middle<down and middle<up and middle<down:
				size = get_basin_size(grid, i_num, i_row)
				sizes.append(size)
				total_res += middle + 1
	return total_res, sizes

if __name__ == "__main__":
	vents = load_data("input.txt")
	add_borders(vents, 9)
	result = find_basins(vents)
	score = result[0]
	sizes = sorted(result[1])[-3:]
	print("score: ", score)
	print("sizes: ", math.prod(sizes))


