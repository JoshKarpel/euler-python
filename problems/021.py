import time
from math import sqrt
from math import ceil


def d(n):
	factors = set()
	for divisor in range(1, ceil(sqrt(n))):
		if n % divisor == 0:
			factors.add(divisor)
			factors.add(int(n / divisor))
	return sum(factors) - n


start_time = time.clock()

amicable = set()

for a in range(1, 10001):
	#print(a)
	da = d(a)
	for b in range(a, 10001, 2):
		#print(a,b)
		db = d(b)
		if da == b and db == a and a != b:
			print(a, da, b, db)
			amicable.add(a)
			amicable.add(b)

print(amicable)
print(len(amicable))
print(sum(amicable))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
