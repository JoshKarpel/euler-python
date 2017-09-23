import itertools


def solve():
    permutations = sorted(itertools.permutations('0123456789'))

    return int(''.join(permutations[999999]))


if __name__ == '__main__':
    print(solve())
