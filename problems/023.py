import itertools

from problems import mymath


def is_abundant(n):
    return sum(mymath.proper_factorization(n)) > n


def solve():
    upper_bound = 28123

    abundant_numbers = (test for test in range(1, upper_bound + 1) if is_abundant(test))
    abundant_sums = {i + j for i, j in itertools.combinations_with_replacement(abundant_numbers, r = 2)}

    return sum(set(range(1, upper_bound + 1)).difference(abundant_sums))


if __name__ == '__main__':
    print(solve())
