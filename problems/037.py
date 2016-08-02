import time
import primes

start_time = time.clock()

upper_bound = 1000000

prime_list = primes.find_primes_less_than_n(upper_bound)
truncatabale_primes = []

for prime in prime_list:
    if len(truncatabale_primes) == 11:
        break
    truncatabale = True
    prime_str = str(prime)
    for trunc in range(len(str(prime)) - 1):
        if int(prime_str[:trunc + 1]) not in prime_list or int(prime_str[trunc + 1:]) not in prime_list:
            truncatabale = False
            break
    if truncatabale and len(prime_str) != 1:
        truncatabale_primes.append(prime)
        print(prime)

print(len(truncatabale_primes))
print(truncatabale_primes)
print(sum(truncatabale_primes))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
