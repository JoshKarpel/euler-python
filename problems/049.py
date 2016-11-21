import time
import primes
import miscmath
import itertools as it
import collections
import utils

with utils.Timer() as t:
    upper_bound = 10000

    primes_list = set(n for n in primes.find_primes_less_than_n(upper_bound) if len(str(n)) == 4)
    # print(primes_list)
    # print(len(primes_list))

    permutations = {}

    for prime in primes_list:
        permutations[prime] = set(p for p in [int(''.join(p)) for p in it.permutations(str(prime))] if p in primes_list)

        if len(permutations[prime]) < 3:
            del permutations[prime]

    for p, s in permutations.items():
        for permutation in it.permutations(s, r = 3):
            sort = sorted(permutation)
            if sort[2] - sort[1] == sort[1] - sort[0]:
                print(sort[2] - sort[1])
                print(sort)

print(t)

# for p, c in sorted(permutations.items()):
#     print(p, sorted(c))

# print(len(permutations))

# permutable_primes = {}
# for prime in primes_list:
#     permutations = [int(''.join(p)) for p in it.permutations(str(prime))]
#     permutable_primes[prime] = set()
#     for permutation in permutations:
#         if int(permutation) in primes_list:
#             permutable_primes[prime].add(permutation)
#
# print(permutable_primes)
# print(permutable_primes[1487])
#
# end_time = time.clock()
#
# print('Elapsed Time: ' + str(end_time - start_time))
