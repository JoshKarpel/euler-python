import time
import primes
import math

start_time = time.clock()

upper_bound = 10000

odds = [odd for odd in range(3, upper_bound + 1, 2)]
squares = [2 * (num ** 2) for num in range(math.ceil(math.sqrt(upper_bound / 2)))]
print(odds)
print(squares)

prime_list = primes.find_primes_less_than_n(upper_bound)
print(prime_list)

for odd in odds:
    print(odd)
    if odd in prime_list:
        continue
    for prime in prime_list:
        if odd - prime in squares:
            # print(odd, prime, odd - prime)
            break
    else:
        print('FOUND IT', odd, prime, odd - prime)
        break

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
