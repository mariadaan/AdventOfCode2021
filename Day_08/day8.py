from dataclasses import dataclass
import itertools

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
class Display:
	"""Contains list of 10 signal pattern and 4 digit output values"""
	pattern: list
	pattern_lens: list
	output_chars: list
	output_chars_lens: list

def create_displays(input):
	displays = []
	for line in input:
		parts = line.split(" | ")
		pattern = parts[0].split(" ")
		pattern_lens = []
		output_chars = parts[1].split(" ")
		output_chars_lens = []
		for string in pattern:
			pattern_lens.append(len(string))
		for string in output_chars:
			output_chars_lens.append(len(string))
		d = Display(pattern, pattern_lens, output_chars, output_chars_lens)
		displays.append(d)
	return displays

def count_1478(lengths):
	# 1 = 2 wires
	# 4 = 4 wires
	# 7 = 3 wires
	# 8 = 7 wires
	return (lengths.count(2) + lengths.count(4) + lengths.count(3) + lengths.count(7))

def sort_string(string):
	sorted_chars = sorted(string)
	string = "".join(sorted_chars)
	return string

def sort_input(displays):
	for display in displays:
		for index, item in enumerate(display.pattern):
			display.pattern[index] = sort_string(display.pattern[index])
		for index, item in enumerate(display.output_chars):
			display.output_chars[index] = sort_string(display.output_chars[index])

def contains_all(str, set):
	""" returns 1 if all chars in set are in str """
	for c in set:
		if c not in str: return 0
	return 1

def get_key(val, connections):
	for key, value in connections.items():
		 if val == value:
			 return key
	return "key doesn't exist"

def config_pattern(pattern, pattern_lens):
	connections = {}
	connections[1] = pattern[pattern_lens.index(2)]
	connections[4] = pattern[pattern_lens.index(4)]
	connections[7] = pattern[pattern_lens.index(3)]
	connections[8] = pattern[pattern_lens.index(7)]

	for index, wires in enumerate(pattern_lens):
		if wires == 5:
			if contains_all(pattern[index], connections.get(1)):
				connections[3] = pattern[index]
		if wires == 6:
			if contains_all(pattern[index], connections.get(7)) and contains_all(pattern[index], connections.get(4)):
				connections[9] = pattern[index]
			elif contains_all(pattern[index], connections.get(7)):
				connections[0] = pattern[index]
			else:
				connections[6] = pattern[index]
	for index, wires in enumerate(pattern_lens):
		if wires == 5:
			if contains_all(connections.get(6), pattern[index]):
				connections[5] = pattern[index]
			elif not contains_all(pattern[index], connections.get(1)):
				connections[2] = pattern[index]
	return (connections)

def decypher(display, connections):
	output_values = ""
	for chars in display.output_chars:
		value = get_key(chars, connections)
		output_values = output_values + str(value)
	return output_values


if __name__ == '__main__':
	raw_data = load_data("input.txt")
	displays = create_displays(raw_data)
	sort_input(displays)
	all_digits = []
	for display in displays:
		connections = config_pattern(display.pattern, display.pattern_lens)
		output_values = decypher(display, connections)
		all_digits.append(int(output_values))
	print("result 2: ", sum(all_digits))

