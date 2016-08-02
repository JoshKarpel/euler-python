import time


start_time = time.clock()

diagonals = [1]
spiral_depth = 3

while spiral_depth <= 1001:
	last_number = diagonals[-1]
	diagonals += [last_number + (n * (spiral_depth - 1)) for n in range(1, 5)]
	spiral_depth += 2

print(diagonals)
print(sum(diagonals))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))