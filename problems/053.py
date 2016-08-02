import time
import math
import miscmath


start_time = time.clock()

combination_values = []

for n in range(1, 101):
	for r in range(0, n + 1):
		combination_values.append(miscmath.number_of_combinations(n, r))

print(len(combination_values))

target = [i for i in combination_values if i > 1000000]

print(len(target))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))