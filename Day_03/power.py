# with open('input.txt','r') as numbers:
# 	report = [int(x) for x in numbers]

file = open("input.txt", 'r')
report = file.read().splitlines()

gamma = ""
epsilon = ""
# for line in report:
for i in range(0, 12):
	count_0 = 0
	count_1 = 0
	for j in range(0, len(report)):
		if report[j][i] == '0':
			count_0 += 1
		elif report[j][i] == '1':
			count_1 += 1
	if count_0 > count_1:
		gamma = gamma + '0'
		epsilon = epsilon + '1'
	else:
		gamma = gamma + '1'
		epsilon = epsilon + '0'

int_gamma = int(gamma, 2)
int_epsilon = (int(epsilon, 2))
result = int_gamma * int_epsilon

print(f"Result pt 1: {result}")

ox_numbers = []
co_numbers = []

# oxygen generator
for i in range(0, 12):
	count_0 = 0
	count_1 = 0
	if i == 0:
		report_mod = report
	else:
		report_mod = ox_numbers
	ox_numbers = []
	for j in range(0, len(report_mod)):
		if report_mod[j][i] == '0':
			count_0 += 1
		elif report_mod[j][i] == '1':
			count_1 += 1
	# als meer 0 dan 1 in bit positie
	if count_0 > count_1:
		for k in range(0, len(report_mod)):
			if report_mod[k][i] == '0':
				ox_numbers.append(report_mod[k])
	# als meer 1 dan 0 in bit positie
	elif count_1 > count_0:
		for k in range(0, len(report_mod)):
			if report_mod[k][i] == '1':
				ox_numbers.append(report_mod[k])
	# als evenveel 1 als 0 in bit positie
	elif count_1 == count_0:
		for k in range(0, len(report_mod)):
			if report_mod[k][i] == '1':
				ox_numbers.append(report_mod[k])
	if len(ox_numbers) == 1:
		break

# co2 scrubber
for i in range(0, 12):
	count_0 = 0
	count_1 = 0
	if i == 0:
		report_mod = report
	else:
		report_mod = co_numbers
	co_numbers = []
	for j in range(0, len(report_mod)):
		if report_mod[j][i] == '0':
			count_0 += 1
		elif report_mod[j][i] == '1':
			count_1 += 1
	# als meer 0 dan 1 in bit positie
	if count_0 > count_1:
		for k in range(0, len(report_mod)):
			if report_mod[k][i] == '1':
				co_numbers.append(report_mod[k])
	# als meer 1 dan 0 in bit positie
	elif count_1 > count_0:
		for k in range(0, len(report_mod)):
			if report_mod[k][i] == '0':
				co_numbers.append(report_mod[k])
	# als evenveel 1 als 0 in bit positie
	elif count_1 == count_0:
		for k in range(0, len(report_mod)):
			if report_mod[k][i] == '0':
				co_numbers.append(report_mod[k])
	if len(co_numbers) == 1:
		break

print("ox_numbers", ox_numbers)
print("co_numbers", co_numbers)

int_ox = int(ox_numbers[0], 2)
int_co = (int(co_numbers[0], 2))

result = int_ox * int_co

print(f"Result pt 2: {result}")