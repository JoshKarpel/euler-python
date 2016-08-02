import time


start_time = time.clock()

n = 0
found = 0
triangular = set()
pentagonal = set()
hexagonal = set()

while found < 3:
	n += 1
	triangular.add(int(n * (n + 1) / 2))
	pentagonal.add(int(n * ((3 * n) - 1) / 2))
	hexagonal.add(int(n * ((2 * n) - 1)))
	intersect = triangular.intersection(pentagonal).intersection(hexagonal)
	if len(intersect) > found:
		found += 1
		print(sorted(intersect))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))