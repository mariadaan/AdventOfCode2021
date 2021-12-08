import statistics as stat

def load_data(filename):
	with open(filename) as f:
		int_array = [int(num.strip()) for num in f.read().split(',')]
	return int_array

def calc_dist(positions, median):
	dists = []
	for pos in positions:
		dist = abs(pos-median)
		dists.append(dist)
	return dists

def natural_numbers(n):
	return int(n * (n + 1) / 2)

def calc_fuel(dists, dest):
	fuel_costs = []
	for dist in dists:
		fuel_costs.append(natural_numbers(dist))
	return fuel_costs

def total_fuel(positions, dest):
	dists = calc_dist(positions, dest)
	fuel_costs = calc_fuel(dists, dest)
	result = sum(fuel_costs)
	return result

def best_of_3(positions, dest):
	dest_tries = [dest - 1, dest, dest + 1]
	results = []
	for dest in dest_tries:
		result = total_fuel(positions, dest)
		results.append(result)
	return min(results)

if __name__ == '__main__':
	positions = load_data("input.txt")
	median = int(stat.median(positions))
	result_1 = total_fuel(positions, median)
	print("result pt 1: ", result_1)

	average = int(round(stat.mean(positions)))
	result_2 = best_of_3(positions, average)
	print("result pt 2: ", result_2)