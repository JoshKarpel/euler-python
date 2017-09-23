from collections import deque

from problems import primes


def solve():
    target_length = 4

    test = 0
    distinct_factor_lens = deque(maxlen = target_length)

    while True:
        test += 1
        distinct_factor_lens.append(len(set(primes.prime_factorization(test))))
        if all(x == target_length for x in distinct_factor_lens):
            return test - target_length + 1


if __name__ == '__main__':
    print(solve())
