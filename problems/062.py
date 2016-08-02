import time
import miscmath


start_time = time.clock()

upper_bound = 1000

permutations_set = dict()
permutations_included = []
cubes = {str(i ** 3) for i in range(1, upper_bound)}

for test_index in range(1, upper_bound):
	test_cube = test_index ** 3
	intersect = set(miscmath.permutations(str(test_cube))).intersection(cubes)
	print(test_index, test_cube, intersect)
	if len(intersect) == 5:
		print(test_index, test_cube, intersect)
		break

print(permutations_set)
print(permutations_included)

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))