import time
import miscmath


def collatz_length(n, length_dictionary):
	current = n
	length = 1
	while current != 1:
		if current in length_dictionary:
			length += length_dictionary[current] - 1
			break
		elif current % 2 == 0:
			current /= 2
		else:
			current = 3 * current + 1
		length += 1
	return length


start_time = time.clock()

collatz_lengths = dict()

for i in range(1, 1000001):
	collatz_lengths[i] = collatz_length(i, collatz_lengths)

num = miscmath.key_of_max_value(collatz_lengths)
print(num, collatz_lengths[num])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
