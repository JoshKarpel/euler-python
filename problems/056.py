import time
import miscmath


def digit_sum(n):
	return sum([int(i) for i in str(n)])

start_time = time.clock()

digit_sums = dict()

for a in range(1, 101):
	for b in range(1, 101):
		digit_sums[(a, b)] = digit_sum(a ** b)

max_key = miscmath.key_of_max_value(digit_sums)

print(max_key, digit_sums[max_key])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))