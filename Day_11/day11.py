import copy

def print_2D(double_array):
	""" Print 2D array """
	for row in double_array:
		print(row)
	print()

def print_2D_noborders(grid):
	""" Print 2D array """
	grid_height = len(grid)
	grid_width = len(grid[0])
	for i_row in range(1, grid_height - 1):
		for i_num in range(1, grid_width - 1):
			print(grid[i_row][i_num], end = '')
		print()
	print()

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
	framed = copy.deepcopy(grid)
	grid_height = len(framed)
	n = len(framed[0]) + 2
	top_bottom = [pad] * n
	for i in range(grid_height):
		framed[i].insert(0, pad)
		framed[i].append(pad)
	framed.insert(0,top_bottom)
	framed.append(top_bottom)
	return framed

def count_2D(grid, value):
	count = 0
	for row in grid:
		count += row.count(value)
	return count 

def increment_all(grid, value):
	grid_height = len(grid)
	grid_width = len(grid[0])
	for i_row in range(1, grid_height - 1):
		for i_num in range(1, grid_width - 1):
			grid[i_row][i_num] += value

def change_all(grid, condition, value):
	grid_height = len(grid)
	grid_width = len(grid[0])
	for i_row in range(1, grid_height - 1):
		for i_num in range(1, grid_width - 1):
			if grid[i_row][i_num] >= condition:
				grid[i_row][i_num] = value

def flash(grid, x, y):
	grid[y][x - 1] += 1
	grid[y - 1][x - 1] += 1
	grid[y - 1][x] += 1
	grid[y - 1][x + 1] += 1
	grid[y][x + 1] += 1
	grid[y + 1][x + 1] += 1
	grid[y + 1][x] += 1
	grid[y + 1][x - 1] += 1

def increment_adjacents(grid):
	newflash = 0
	grid_height = len(grid)
	grid_width = len(grid[0])
	for y in range(1, grid_height - 1):
		for x in range(1, grid_width - 1):
			if grid[y][x] == 0 or grid[y][x] >= 10:
				continue
			left = grid[y][x - 1]
			upleft = grid[y - 1][x - 1]
			up = grid[y - 1][x]
			upright = grid[y - 1][x + 1]
			right = grid[y][x + 1]
			downright = grid[y + 1][x + 1]
			down = grid[y + 1][x]
			downleft = grid[y + 1][x - 1]
			adjacents = [left, upleft, up, upright, right, downright, down, downleft]
			flash_count = adjacents.count(0)
			grid[y][x] += flash_count
			if grid[y][x] >= 10:
				newflash += 1
				# grid[y][x] = 0
	change_all(grid, 10, 0)
	return newflash


def take_step(grid):
	increment_all(grid, 1)
	change_all(grid, 10, 0)
	newflash = 1
	while newflash:
		newflash = increment_adjacents(grid)
	flashes = count_2D(grid, 0)
	return flashes

def simulate_steps(grid, steps):
	flashes = 0
	for step in range(steps):
		flashes += take_step(grid)
		print(f"After step {step + 1}")
		print_2D_noborders(grid)
	return flashes

if __name__ == "__main__":
	octos = load_data("sample.txt")
	octos_bordered = add_borders(octos, -1)
	print("Before any steps:")
	print_2D_noborders(octos_bordered)
	steps = 6
	flashes = simulate_steps(octos_bordered, steps)
	print("flashes: ", flashes)