from math import sqrt
import collections

from problems import utils


@utils.memoize
def pentagon(n):
    return int(n * ((3 * n) - 1) / 2)


def solve():
    upper_bound = 3000
    pentagons = set((pentagon(n) for n in range(1, upper_bound)))
    for n in range(1, upper_bound):
        p_n = pentagon(n)
        for m in range(1, n):
            p_m = pentagon(m)

            if p_n - p_m in pentagons and p_n + p_m in pentagons:
                return p_n - p_m


if __name__ == '__main__':
    print(solve())
