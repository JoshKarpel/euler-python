import time
import miscmath
import primes

divisors = primes.find_n_primes(10)

def divisibility_test(n):
	divisor_strings = [int(str(n)[i:i + 3]) for i in range(1, 8)]
	check = [int(divisor_strings[i] / divisors[i]) == divisor_strings[i] / divisors[i] for i in range(0, 7)]
	return miscmath.list_product(check)

#print(divisibility_test(1406357289))

start_time = time.clock()

permutations = [int(i) for i in miscmath.permutations('0123456789')]

numbers = []

for test in permutations:
	try:
		if divisibility_test(test):
			numbers.append(test)
	except IndexError:
		pass

print(numbers)
print(len(numbers))
print(sum(numbers))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))