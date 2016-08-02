import time
import primes

start_time = time.clock()

print(primes.find_n_primes(10001))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time-start_time))
