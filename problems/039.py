import time


start_time = time.clock()

triplet_counts = {i: 0 for i in range(1, 1001)}

for perimeter in range(3, 1001):
	print(perimeter)
	for a in range(1, perimeter):
		for b in range(1, perimeter - a):
			c = perimeter - a - b
			if a ** 2 + b ** 2 == c ** 2:
				triplet_counts[perimeter] += 1
				#print(a, b, c, a + b + c)
	#print(triplet_counts[perimeter])

print(triplet_counts)

num = max(triplet_counts, key = triplet_counts.get)
print(num, triplet_counts[num])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))