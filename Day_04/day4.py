
def board_has_bingo(board):
	for row in board:
		hor_sum = 0
		for number in row:
			hor_sum += number
		if hor_sum == -5:
			return 1
	for j in range(5):
		vert_sum = 0
		for i in range(5):
			vert_sum += board[i][j]
		if vert_sum == -5:
			return 1
	return 0

def count_bingo(all_boards):
	count = 0
	for board in all_boards:
		if board_has_bingo(board):
			count += 1
	return count

def find_last_board(all_boards):
	for board in all_boards:
		if board_has_bingo(board) == 0:
			return board

# def is_bingo(all_boards, winning_boards):
# 	hor_sum = 0
# 	vert_sum = 0
# 	board_num = 0
# 	for board in all_boards:
# 		if board_has_bingo(board) and board not in winning_boards:
# 			winning_boards.append(board_num)
# 			print("BOARD NUM: ", board_num)
# 			# return board_num
# 		board_num += 1
# 	return winning_boards


def calc_result(board):
	total = 0
	for row in board:
		for num in row:
			if num != -1:
				total += num
	print("total: ", total)
	return total


file = open("input.txt", 'r')
bingo = file.read().splitlines()

first_line = bingo[0]
balls = first_line.split(",")
balls = [int(x) for x in balls]
boards = bingo[2:]
all_boards = []
len_boards = len(boards)
j = 0
while j < len_boards:
	one_board = []
	for i in range(5):
		line = boards[i + j]
		line = line.replace("  ", " ")
		line = line.strip()
		line = line.split(" ")
		numbers = [int(x) for x in line]
		one_board.append(numbers)
	all_boards.append(one_board)
	j += 6

i_boards = 0
i_rows = 0
i_numbers = 0
bingo_count = 0
last_board = []
for ball in balls:
	i_boards = 0
	i_rows = 0
	i_numbers = 0
	for board in all_boards:
		i_rows = 0
		i_numbers = 0
		for row in board:
			i_numbers = 0
			for number in row:
				if number == ball:
					all_boards[i_boards][i_rows][i_numbers] = -1
				i_numbers += 1
			i_rows += 1
		i_boards += 1
	bingo_count = count_bingo(all_boards)
	if bingo_count == 99:
		last_board = find_last_board(all_boards)
	if bingo_count == 100:
		total = calc_result(last_board)	
		print("winning board: ", last_board)
		print("winning_num:   ", ball)
		final_result = total * ball
		print("final result: ", final_result)
		exit()

	# board_num = is_bingo(all_boards)
	# winning_boards = is_bingo(all_boards, winning_boards)
	# print("\n\nWINNING BOARDS: ")

	# for winning_board in winning_boards:
	# 	bingo_count += 1
	# 	print("\nbingo count: ", bingo_count)
	# 	total = calc_result(all_boards[winning_board])
	# 	# print("\nboard num: ", board_num)
	# 	print("winning board: ", all_boards[winning_board])
	# 	print("winning_num:   ", ball)
	# 	final_result = total * ball
	# 	print("final result: ", final_result)
	# 	print("len win boards: ", len(winning_boards))
	# 	if len(winning_boards) >= 100:
	# 		exit()



# print("winning_num:   ", 10)
# total = calc_result(all_boards[90])
# final_result = total * 10
# print("final result: ", final_result)

# 99 54 74 83 92
# 27 53 15  8 85
# 94 36 63 29 91
# 58 10 45 38 79
#  9 95 23 98 33

# 67,31,58,8,79,18,19,45,38,13,40,62,85,10,21,96,56,55,4,36,76,42,32,34,39,89,6,12,24,57,93,47,41,52,83,61,