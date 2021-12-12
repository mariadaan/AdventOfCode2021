import statistics as stat

def print_2D(double_array):
	""" Print 2D array """
	for row in double_array:
		print(row)

def load_data(filename):
	""" Loads data as 2d array """
	file = open(filename, 'r')
	data = file.read().splitlines()
	return data

def set_in_str(string, sets):
	for item in sets:
		if item in string:
			return 1
	return 0

def remove_sets(chunks):
	stripped = []
	sets = ["{}", "[]", "()", "<>"]
	for index, row in enumerate(chunks):
		while set_in_str(row, sets):
			row = row.replace("{}", "")
			row = row.replace("()", "")
			row = row.replace("<>", "")
			row = row.replace("[]", "")
		stripped.append(row)
	return stripped

def reverse_strings(chunks):
	reversed = []
	for row in chunks:
		row = row[::-1]
		row = row.replace('{', '}')
		row = row.replace('(', ')')
		row = row.replace('<', '>')
		row = row.replace('[', ']')
		reversed.append(row)
	return reversed

def remove_extras(chunks):
	stripped = chunks
	sets = ['>', '}', ']', ')']
	for row in chunks:
		if set_in_str(row, sets):
			stripped.remove(row)
	return stripped


def find_errors(chunks):
	only_incompletes = chunks.copy()
	illegal_chars = []
	closers = ">}])"
	for row in chunks:
		# print("row: ", row)
		for char in row:
			if char in closers:
				illegal_chars.append(char)
				only_incompletes.remove(row)
				break
	# only_incompletes = remove_extras(only_incompletes)
	missing_part = reverse_strings(only_incompletes)
	# print(illegal_chars)
	return illegal_chars, missing_part

def get_scores_1(chars):
	scores = []
	for char in chars:
		char = char.replace(')', "3")
		char = char.replace(']', "57")
		char = char.replace('}', "1197")
		char = char.replace('>', "25137")
		scores.append(int(char))
	return scores

def get_scores_2(missing_part):
	for index, line in enumerate(missing_part):
		missing_part[index] = list(line)
	scores = []
	for row in missing_part:
		score = 0
		for bracket in row:
			bracket = bracket.replace(')', '1')
			bracket = bracket.replace(']', '2')
			bracket = bracket.replace('}', '3')
			bracket = bracket.replace('>', '4')
			score = score * 5 + int(bracket)
		scores.append(score)
	return scores

if __name__ == "__main__":
	chunks = load_data("input.txt")
	chunks = remove_sets(chunks)
	results = find_errors(chunks)
	illegal_chars = results[0]
	scores_1 = get_scores_1(illegal_chars)
	print("score 1: ", sum(scores_1))

	missing_part = results[1]
	scores_2 = get_scores_2(missing_part)
	score_2 = int(stat.median(scores_2))
	print("score 2: ", score_2)
