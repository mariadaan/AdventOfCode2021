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
	"""Contains list of 10 signal patterns and 4 digit output values"""
	patterns: list
	outputs: list
	dig_lens: list

def create_displays(input):
	displays = []
	dig_lens = []
	for line in input:
		parts = line.split(" | ")
		parts[0] = parts[0].split(" ")
		parts[1] = parts[1].split(" ")
		for string in parts[1]:
			dig_lens.append(len(string))
		d = Display(parts[0], parts[1], dig_lens)
		displays.append(d)
	return displays

def count_1478(lengths):
	# 1 = 2 wires
	# 4 = 4 wires
	# 7 = 3 wires
	# 8 = 7 wires
	return (lengths.count(2) + lengths.count(4) + lengths.count(3) + lengths.count(7))

def get_digits(outputs):
	for index, item in enumerate(outputs):
		if (len(item) == 2): # 1 = 2 wires
			outputs[index] = '1'
		elif (len(item) == 4): # 4 = 4 wires
			outputs[index] = '4'
		elif (len(item) == 3): # 7 = 3 wires
			outputs[index] = '7'
		elif (len(item) == 7): # 8 = 7 wires
			outputs[index] = '8'
		elif (len(item) == 5): # 2, 3, 4 = 5 wires
			if 'e' in item: # 5 = defbc
				outputs[index] = '5' 
			elif 'b'in item: # 3 = dafbc
				outputs[index] = '3'
			else: # 2 = dafgc
				outputs[index] = '2'
		elif (len(item) == 6):
			if 'g' not in item: # 9 = fdcagb
				outputs[index] = '9'
			elif 'a' in item: # 0 = cagedb
				outputs[index] = '0'
			else:
				outputs[index] = '6'
	outputs = int("".join(outputs))
	return outputs

if __name__ == '__main__':
	raw_data = load_data("sample.txt")
	displays = create_displays(raw_data)
	result_1 = count_1478(displays[-1].dig_lens)
	print("result 1: ", result_1)

	all_digits = []
	for display in displays:
		real_digits = get_digits(display.outputs)
		all_digits.append(real_digits)
	print_2D(all_digits)
	print("result 2: ", sum(all_digits))
