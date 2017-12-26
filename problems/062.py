import itertools
import collections

from problems import utils, mymath, primes


def is_cube(n):
    counter = collections.Counter(primes.prime_factorization(n))

    return all(v % 3 == 0 for v in counter.values())


def solve():
    upper_bound = 1000

    for c in range(upper_bound):
        cube = c ** 3
        perms = set(int(''.join(n)) for n in itertools.permutations(str(cube)))
        num_cube_perms = len([n for n in perms if is_cube(n)])

        if num_cube_perms == 3:
            return cube


if __name__ == '__main__':
    print(solve())
