# 0 wordt 6 en creeert een 8
# eens in de 6 keer komt er een bij
# voor deze nieuwe eerste keer na 8 keer pas nieuwe bij
# daarna weer eens in de 6 keer

# 3 4 3 1 2
# [0][1][2][3][4][5][6][7][8]
# [0, 1, 1, 2, 1, 0, 0, 0, 0]

# counted_fishies[0] is hoeveel nieuwe erbij gaan komen
# alles verplaatst 1 stap naar links want timer loopt 1 dag af
# couned_fishies[6] doe je dus plus counted_fishies[0]
# counted_fishies[8] is gelijk aan het aantal nieuwe vissies


def load_data(filename):
	"""
	Loads data as 2d array
	"""
	with open(filename,'r') as numbers:
		data = [int(x) for x in numbers]
	return data

def pass_day(fishies):
	"""
	Decrease timer. If 0, become 6 and add 8
	"""
	i_fish = 0
	for fish in fishies:
		if fish == 0:
			fishies[i_fish] = 6
			fishies.append(9)
		else:
			fishies[i_fish] -= 1
		i_fish += 1
	return fishies

def calc_fishamount(fishies, days):
	counted_fishies = [fishies.count(i) for i in range(9)]
	for _ in range(days):
		spawned_count = counted_fishies[0]
		counted_fishies[:-1] = counted_fishies[1:]
		counted_fishies[6] += spawned_count
		counted_fishies[8] = spawned_count 
	return sum(counted_fishies)

if __name__ == '__main__':
	fishies = load_data('input.txt')
	days = 80
	# print(f"init 0: {fishies}")
	for day in range(1, int(days) + 1):
		fishies = pass_day(fishies)
		# print(f"day {day}: {fishies}")
	fishies_amount = len(fishies)
	fishies = load_data('input.txt')
	print(f"there are {fishies_amount} fishies after {days} days")
	days = 256
	fishies_amount = calc_fishamount(fishies, days)
	print(f"there are {fishies_amount} fishies after {days} days")
