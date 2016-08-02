import time
import primes

start_time = time.clock()

factors = primes.prime_factorization(600851475143)
print(factors)

end_time = time.clock()

print('Elapsed Time: ' + str(end_time-start_time))
