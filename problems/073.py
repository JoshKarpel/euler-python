import time
import miscmath
import math
from fractions import Fraction


def solve():
    max_denominator = 12000

    lower = 1 / 3
    upper = 1 / 2

    fractions_list = set([Fraction(n, d) for d in range(2, max_denominator + 1) for n in range(int(math.floor(d / 3) - 1), int(math.ceil(d / 2) + 1)) if lower < n / d < upper])
    return len(fractions_list)


if __name__ == '__main__':
    print(solve())
