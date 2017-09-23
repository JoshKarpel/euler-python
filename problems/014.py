from . import mymath, utils


@utils.memoize
def collatz_length(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + collatz_length(n / 2)
    else:
        return 1 + collatz_length((3 * n) + 1)


def solve():
    collatz_lengths = {x: collatz_length(x) for x in range(1, 1000001)}

    return mymath.key_of_max_value(collatz_lengths)
