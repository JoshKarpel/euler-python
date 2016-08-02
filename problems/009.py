import time

start_time = time.clock()

target = 1000

largest_product = 0

for a in range(1, target):
	for b in range(1, target - a):
		c = target - a - b
		#print(a,b,c,a+b+c)
		if a ** 2 + b ** 2 == c ** 2:
			print(a, b, c, a + b + c, a * b * c)
end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))