import time
import primes


def period(n):
    test = 0
    while True:
        # print(test)
        test += 1
        if (10 ** test) % n == 1:
            return test

start_time = time.clock()

for n in primes.find_primes_less_than_n(1000)[4:]:
    print(n, 1 / n, period(n))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
