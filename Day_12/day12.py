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

def dfs(visited, neighbours, cave, first = 0):
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
		dfs(visited, neighbours, next_cave)
	if cave.islower():
		visited.remove(cave)
	return

if __name__ == "__main__":
	global paths
	paths = 0
	data = load_data("input.txt")
	connections = create_dict(data)
	# print(dict(connections))
	# print()
	visited = set()
	dfs(visited, connections, "start", 1)
	print(paths)
