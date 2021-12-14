from itertools import product
import re

def print_2D(double_array):
	""" Print 2D array """
	for row in double_array:
		print(row)

def load_data(filename):
	""" Loads data as 2d array """
	file = open(filename, 'r')
	data = file.read().splitlines()
	uniques = []
	for index, row in enumerate(data):
		data[index] = row.split('-')
		for elem in data[index]:
			if elem not in uniques:
				uniques.append(elem)
		data[index] = tuple(data[index])
	uniques.insert(0, uniques.pop(uniques.index("start")))
	uniques.append(uniques.pop(uniques.index("end")))
	return data, uniques

def find_other(tupleset, value):
	other = 0
	try :
		pos = tupleset.index(value)
		if pos == 0:
			other = tupleset[1]
		elif pos == 1:
			other = tupleset[0]
	except ValueError:
		return 0
	return other

def find_nexts(connections, value):
	next_points = []
	for con in connections:
		other = find_other(con, value)
		if other:
			next_points.append(other)
	return next_points

def remove_duplicates(all_paths):
	new_paths = []
	for path in all_paths:
		new_paths.append(",".join(path))
	# print(new_paths)
	return list(dict.fromkeys(new_paths))

def createaa_paths(uniques, connections, big_caves, small_caves):
	all_paths = [["start"]]
	path_len = len(uniques)
	for i in range(path_len):
		for index in range(len(all_paths)):
			next_points = find_nexts(connections, all_paths[index][-1])
			for point in next_points:
				new_path = all_paths[index].copy()
				if point == "end" or (point in small_caves and point in new_path):
					continue
				new_path.append(point)
				all_paths.append(new_path)
	# correct_paths = []
	# for row in all_paths:
	# 	if row[-1] == 'end':
	# 		correct_paths.append(row)
	# all_paths.clear()
	print_2D(all_paths)
	new_list = remove_duplicates(all_paths)
	return new_list

def create_paths(uniques, connections, big_caves, small_caves):
	all_paths = [["start"]]
	path_len = len(uniques) + 3
	for i in range(path_len):
		for index in range(len(all_paths)):
			next_points = find_nexts(connections, all_paths[index][-1])
			for point in next_points:
				new_path = all_paths[index].copy()
				if point == "end" or (point in small_caves and point in new_path):
					continue
				new_path.append(point)
				all_paths.append(new_path)
	new_list = remove_duplicates(all_paths)
	correct_paths = []
	end_points = find_nexts(connections, "end")
	for path in new_list:
		if path[-2:] in end_points:
			correct_paths.append(path + ",end")
	return correct_paths

# def create_paths(uniques, connections, big_caves, small_caves):
# 	all_paths = ["start,"]
# 	path_len = len(uniques)
# 	for i in range(path_len):
# 		for index in range(len(all_paths)):
# 			last = all_paths[index].rsplit(',', 1)[1]
# 			print(last)
# 			next_points = find_nexts(connections, last)
# 			print(next_points)
# 			for point in next_points:
# 				new_path = all_paths[index]
# 				if point in small_caves and point in new_path:
# 					continue
# 				new_path = new_path + ',' + point
# 				all_paths.append(new_path)
# 	# correct_paths = []
# 	# for row in all_paths:
# 	# 	if row[-1] == 'end':
# 	# 		correct_paths.append(row)
# 	# new_list = remove_duplicates(correct_paths)
# 	# return new_list
# 	return all_paths

def get_caves(uniques):
	small_caves = []
	big_caves = []
	for cave in uniques:
		if cave.islower():
			small_caves.append(cave)
		else:
			big_caves.append(cave)
	return small_caves, big_caves


if __name__ == "__main__":
	result = load_data("input.txt")
	connections = result[0]
	uniques = result[1]
	result = get_caves(uniques)
	small_caves = result[0]
	big_caves = result[1]
	paths = create_paths(uniques, connections, big_caves, small_caves)
	# print_2D(paths)
	print(len(paths))
