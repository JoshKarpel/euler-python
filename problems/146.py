import time
import primes

start_time = time.clock()

upper_bound = 10**7
primes_list = primes.find_primes_less_than_n(upper_bound)

print(len(primes_list))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))