import time


start_time = time.clock()

sequence = set()

for a in range(2, 101):
	for b in range(2, 101):
		sequence.add(a ** b)

print(len(sequence))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))