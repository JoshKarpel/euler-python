import time
import primes
import miscmath

start_time = time.clock()

test = 0
prime_factorization_lengths = [0, 0, 0, 0, 0, 0]
target_length = 4

while True:
    test += 1
    print(test)
    prime_factorization_lengths.append(len(set(primes.prime_factorization(test))))
    if miscmath.list_product([prime_factorization_lengths[-1 - i] == target_length for i in range(0, target_length)]):
        print('FOUND IT', sorted([test - i for i in range(0, target_length)]))
        break


end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
