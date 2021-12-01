
def count_increases(int_array):
	counter = 0
	for i in range(len(int_array) - 1):
		if int_array[i + 1] > int_array[i]:
			counter += 1
	return counter

def three_measurement(int_array):
	three_sum_array = []
	i = 1
	while i < (len(depths) - 1):
		value = depths[i - 1] + depths[i] + depths[i + 1]
		three_sum_array.insert(i - 1, value)
		i += 1
	return three_sum_array

with open('input.txt','r') as numbers:
	depths = [int(x) for x in numbers]

increases = count_increases(depths)
print("Part 1 answer: ", increases)

three_sum_array = three_measurement(depths)
increases = count_increases(three_sum_array)

print("Part 2 answer: ", increases)