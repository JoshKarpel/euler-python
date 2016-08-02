import time
import primes
import miscmath
import itertools as it

start_time = time.clock()

upper_bound = 10000

primes_list = [n for n in primes.find_primes_less_than_n(upper_bound) if len(str(n)) == 4]
#print(primes_list)
print(len(primes_list))

permutable_primes = {}
for prime in primes_list:
    permutations = [int(''.join(p)) for p in it.permutations(str(prime))]
    permutable_primes[prime] = set()
    for permutation in permutations:
        if int(permutation) in primes_list:
            permutable_primes[prime].add(permutation)

print(permutable_primes)
print(permutable_primes[1487])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))