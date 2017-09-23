import itertools


def solve():
    return len({a ** b for a, b, in itertools.product(range(2, 101), repeat = 2)})
