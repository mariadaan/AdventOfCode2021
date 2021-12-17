from collections import defaultdict

def load_data(filename):
	""" 
	Load data as 2d array
	"""
	with open(filename) as file:
		raw_data = file.read().strip()
	data = [row.split("-") for row in raw_data.split("\n")]
	return data

def create_dict(data):
	"""
	in: 2D array in format
		[['start', 'A'], ['start', 'b']]
	out: Dict to act as an adjacency list in format
		{'start':	['A', 'b'],
		'A'	 		['start', 'c', 'b', 'end'],
		'b':		['start', 'A', 'd', 'end'],
		'c':		['A'], 'd': ['b'],
		'end':		['A', 'b']}
	 """
	connections = defaultdict(list)
	for a, b in data:
		# punt a is de naam van het punt, 
		# b is waar je naartoe kan vanaf punt a
		# maak met connections[a] nieuw element in dict met key a
		# voeg met .append(b) connected punt toe aan lijst van values die bij key a horen
		# als connection[a] al bestaat wordt er geen nieuw element met key a aangemaakt,
		# maar wordt nog een bestemming toegevoegd aan de connections met dat punt
		# andersom ook toevoegen want de connecties werken twee richtingen op
		connections[a].append(b)
		connections[b].append(a)
	return connections

def dfs(visited, neighbours, cave):
	"""
	Depth-first search: algorithm for tree traversal on graph or tree data structures.
	"""
	global paths

	if cave == "end":
		paths += 1
		return
	if cave in visited and cave.islower():
		return
	if cave.islower():
		visited.add(cave) 
	for next_cave in neighbours[cave]:
		# dont go back to start
		if next_cave == "start":
			continue
		# keep going to next cave with recursion, until "end" is reached
		dfs(visited, neighbours, next_cave)
	# remove last visited cave in current path from visited set when stepping back in recursion depth
	if cave.islower():
		visited.remove(cave)
	return

def has_duplicates(lst):
	""" Check if given list contains any duplicates """
	if len(lst) == len(set(lst)):
		return False
	else:
		return True

def find_duplicate(lst):
	count_item = 0
	for item in lst:
		for dup in lst:
			if item == dup:
				count_item += 1
		if count_item > 1:
			return item
	return 0

def most_common(lst):
	if len(lst) > 0:
		return max(set(lst), key=lst.count)
	else:
		return 0

def count_item(lst, item):
	return lst.count(item)

# check if one of the items is in the list 2 times
def check_counts(lst, cave):
	item = most_common(lst)
	common_count = count_item(lst, item)
	if lst.count(cave) == 1 and common_count == 2:
		return True
	else:
		return False

def dfs2(visited, neighbours, cave):
	"""
	Depth-first search: algorithm for tree traversal on graph or tree data structures.
	"""
	global paths

	if cave == "end":
		paths += 1
		return
	if visited.count(cave) == 2 or check_counts(visited, cave):
		return
	if cave.islower():
		visited.append(cave) 
	for next_cave in neighbours[cave]:
		# dont go back to start
		if next_cave == "start":
			continue
		# keep going to next cave with recursion, until "end" is reached
		dfs2(visited, neighbours, next_cave)
	# remove last visited cave in current path from visited set when stepping back in recursion depth
	if cave.islower():
		visited.remove(cave)
	return


if __name__ == "__main__":
	global paths
	paths = 0
	data = load_data("input.txt")
	#print(data)
	connections = create_dict(data)
	# print(connections)

	# part 1
	visited = set()
	dfs(visited, connections, "start")
	print(paths)

	# part 2
	paths = 0
	visited = []
	dfs2(visited, connections, "start")
	print()
	print(paths)
