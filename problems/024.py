from . import mymath


def solve():
    permutations = sorted(mymath.permutations('0123456789'))

    return permutations[999999]
