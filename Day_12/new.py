from collections import defaultdict, deque
from pprint import pprint

def load_data(filename):
	""" 
	Load data as 2d array
	"""
	with open("minisample.txt") as file:
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



def dfs(visited, graph, cave):
	
	paths = 0

	if cave == "end":
		paths += 1
		return
	for neighbour in graph[cave]:
		# dont go back to start
		if neighbour == "start" or (cave.islower() and cave in visited) or cave.isupper():
			print("test")
			visited.append(cave)
			visited = dfs(visited, graph, neighbour)
	print(paths)
	return visited

if __name__ == "__main__":
	data = load_data("minisample.txt")
	connections = create_dict(data)
	visited = set()
	visited = dfs(visited, connections, "start")
	print(visited)
