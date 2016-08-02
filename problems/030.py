import time


def digit_power_sum(n, power):
	return sum([int(i) ** power for i in str(n)])


start_time = time.clock()

upper_bound = 999999

#print(digit_power_sum(1634, 4))
#print(digit_power_sum(8208, 4))
#print(digit_power_sum(9474, 4))

answers = set()

for n in range(2, upper_bound + 1):
	if n == digit_power_sum(n, 5):
		print(n)
		answers.add(n)

print(answers)
print(sum(answers))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))