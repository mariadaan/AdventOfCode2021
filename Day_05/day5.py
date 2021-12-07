from dataclasses import dataclass

def print_2D(double_array):
	for row in double_array:
		print(row)

def load_data(filename):
	"""
	Loads data as 2d array
	"""
	file = open(filename, 'r')
	data = file.read().splitlines()
	return data

@dataclass
class Line:
	"""Class for keeping track of lines start and end point."""
	x_1: int
	y_1: int
	x_2: int
	y_2: int

def create_points(input):
	points = []
	for line in input:
		line = line.replace(" -> ", ",")
		splitted = line.split(",")
		x1 = int(splitted[0])
		y1 = int(splitted[1])
		x2 = int(splitted[2])
		y2 = int(splitted[3])
		p = Line(x1, y1, x2, y2)
		points.append(p)
	return points

def create_map(points):
	# find highest x and highest y coordinate
	# create map with that y value + 1 as amount of rows
	# create map with that x value + 1 as amount of columns

	highest_x = 0
	highest_y = 0
	for point in points:
		if point.x_1 > highest_x:
			highest_x = point.x_1
		elif point.x_2 > highest_x:
			highest_x = point.x_2
		if point.y_1 > highest_y:
			highest_y = point.y_1
		elif point.y_2 > highest_y:
			highest_y = point.y_2
	zeroes_map = [ [0] * (highest_x + 1) for _ in range(highest_y + 1)]
	return zeroes_map

def draw_straight(my_map, point):
	if point.x_1 == point.x_2: # vertical lines
		start_y = min(point.y_1, point.y_2)
		end_y = max(point.y_1, point.y_2)
		for y_iter in range(start_y, end_y + 1):
			my_map[y_iter][point.x_1] = my_map[y_iter][point.x_1] + 1

	if point.y_1 == point.y_2: # horizontal lines
		start_x = min(point.x_1, point.x_2)
		end_x = max(point.x_1, point.x_2)
		for x_iter in range(start_x, end_x + 1):
			my_map[point.y_1][x_iter] = my_map[point.y_1][x_iter] + 1
	return my_map

def draw_diagonal(my_map, point):
	if abs(point.x_1 - point.x_2) != abs(point.y_1 - point.y_2):
		return my_map # return if not a diagonal line
	line_len = abs(point.x_1 - point.x_2) + 1
	# is punt 1 of 2 meest links?
	if point.x_1 < point.x_2:
		# punt 1 meest links
		if point.y_1 < point.y_2:
			# punt 2 ligt rechtsonder punt 1
			# left to right down
			for i in range(line_len):
				my_map[point.y_1 + i][point.x_1 + i] = my_map[point.y_1 + i][point.x_1 + i] + 1
		if point.y_1 > point.y_2:
			# punt 2 ligt rechtsboven punt 1
			for i in range(line_len):
				my_map[point.y_1 - i][point.x_1 + i] = my_map[point.y_1 - i][point.x_1 + i] + 1
	else:
		# punt 2 meest links
		if point.y_2 < point.y_1:
			# punt 1 ligt rechtsonder punt 2
			# left to right down
			for i in range(line_len):
				my_map[point.y_2 + i][point.x_2 + i] = my_map[point.y_2 + i][point.x_2 + i] + 1
		if point.y_2 > point.y_1:
			# punt 2 ligt rechtsboven punt 1
			for i in range(line_len):
				my_map[point.y_2 - i][point.x_2 + i] = my_map[point.y_2 - i][point.x_2 + i] + 1
	return my_map


def fill_map(my_map, points):
	for point in points:
		my_map = draw_straight(my_map, point)
		my_map = draw_diagonal(my_map, point)
	return my_map

def calc_overlap(my_map):
	overlap_points = 0
	for row in my_map:
		for num in row:
			if num >= 2:
				overlap_points += 1
	return overlap_points

if __name__ == '__main__':
	vents = load_data("input.txt")
	points = create_points(vents)
	my_map = create_map(points)
	my_map = fill_map(my_map, points)
	overlap_points = calc_overlap(my_map)
	print("Result part 2: ", overlap_points)



