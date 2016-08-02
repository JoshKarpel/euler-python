import time
import miscmath
import primes


start_time = time.clock()

current_primes = []

set_size = 0

for latest_prime in primes.generate_primes():
	if set_size < 4:
		set_size += 1
		current_primes.append(latest_prime)
	else:
		current_primes.pop(0)
		current_primes.append(latest_prime)
		print(current_primes)
		found = True
		for i in range(set_size):
			for j in range(set_size):
				prime_test = int(''.join([str(current_primes[i]), str(current_primes[j])]))
				if not primes.is_prime(prime_test):
					found *= False
		if found:
			print(current_primes)
			print(sum(current_primes))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))