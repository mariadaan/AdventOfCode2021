file = open("input.txt", 'r')
directions = file.read().splitlines()

# PART 1
horizontal = 0
vertical = 0
for line in directions:
	if "forward" in line:
		horizontal += (int)(line[-1])
	elif "down" in line:
		vertical += (int)(line[-1])
	elif "up" in line:
		vertical -= (int)(line[-1])
print("result pt1: ", horizontal * vertical)

# PART 2
aim = 0
horizontal = 0
vertical = 0
for line in directions:
	if "forward" in line:
		horizontal += (int)(line[-1])
		vertical += aim * (int)(line[-1])
	elif "down" in line:
		aim += (int)(line[-1])
	elif "up" in line:
		aim -= (int)(line[-1])

print("result pt2: ", horizontal * vertical)
