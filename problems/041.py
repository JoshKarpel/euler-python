import time
import primes
import miscmath


start_time = time.clock()

digits_sorted = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

upper_bound = str(1234567)

pandigitals = []

for test in reversed(sorted(miscmath.permutations(upper_bound))):
	if primes.is_prime(int(test)) and sorted(test) == digits_sorted[:len(test)]:
		pandigitals.append(int(test))

#print(pandigitals)

print(max(pandigitals))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))