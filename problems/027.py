import time
import primes


start_time = time.clock()

longest = [0, 0, 0]

for b in range(-999, 1000, 2):
	for c in primes.find_primes_less_than_n(1000):
		n = -1
		while True:
			n += 1
			q = n ** 2 + (b * n) + c
			if not primes.is_prime(q) or q <= 1:
				if n > longest[2]:
					longest = [b, c, n, q]
				break

print(longest)
print(longest[0] * longest[1])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))