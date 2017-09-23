import itertools
from problems import primes


def solve():
    digits_sorted = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    upper_bound = str(1234567)

    pandigitals = []

    for test in reversed(sorted(itertools.permutations(upper_bound))):
        num = int(''.join(test))
        if primes.is_prime(num) and sorted(test) == digits_sorted[:len(test)]:
            pandigitals.append(num)

    return max(pandigitals)


if __name__ == '__main__':
    print(solve())
