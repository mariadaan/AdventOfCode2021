import numpy as np
from itertools import product

def load_data(filename):
	""" Load data as 2D int numpy array"""
	with open(filename) as file:
		raw_data = file.read().strip().split("\n")
	data = np.array([[int(x) for x in list(row)] for row in raw_data])
	return data

def increment_all(grid, height, value):
	""" Increment all numbers in grid by value """
	for y, x in product(range(height), repeat=2):
		grid[y, x] += value

def take_step(grid, height):
	flashes = 0
	# create new array with zeroes to save flashed octos
	flashed = np.zeros((height, height), dtype=bool)
	increment_all(grid, height, 1)

	while True:
		keep_going = False

		# save where change has happened
		change = np.zeros((height, height), dtype=int)

		# door alle octo's heen loopen
		for y, x in product(range(height), repeat=2):
			# als octo nog niet geflashed is en octo is >9 flashen
			if not flashed[y, x] and grid[y, x] > 9:
				flashes += 1
				# onthouden dat deze octo geflashed heeft
				flashed[y, x] = True
				keep_going = True

				for dy, dx in product(range(-1, 2), repeat=2):
					if dy == dx == 0:
						continue
					yy = y + dy
					xx = x + dx
					if not (0 <= yy < height and 0 <= xx < height):
						continue
					change[yy, xx] += 1

		grid += change

		if not keep_going:
			break

	for y, x in product(range(height), repeat=2):
		if flashed[y, x]:
			grid[y, x] = 0
	return flashes

def simulate_steps(grid, steps):
	height = len(grid)
	flashes = 0
	for step in range(steps):
		flashes += take_step(grid, height)
		print(f"After step {step + 1}")
		print(grid)
	return flashes

if __name__ == "__main__":
	grid = load_data("sample.txt")
	print(grid)
	flashes = simulate_steps(grid, 10)
	print("flashes: ", flashes)
