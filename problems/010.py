import time
import primes

start_time = time.clock()

primes = primes.find_primes_less_than_n(2000000)

print(sum(primes))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time-start_time))
