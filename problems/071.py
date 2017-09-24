import math
from fractions import Fraction


def solve():
    max_denominator = 1000000

    lower = 428571 / 1000000
    upper = 3 / 7

    fractions_list = sorted(list(set([Fraction(n, d) for d in range(700000, max_denominator + 1) for n in range(428400, int(math.ceil(3 * d / 7))) if lower <= n / d < upper])))

    return fractions_list[-1].numerator


if __name__ == '__main__':
    print(solve())
