import time
from problems import utils
import math


@utils.memoize
def pentagon(n):
    return int(n * ((3 * n) - 1) / 2)


@utils.memoize
def is_pentagon(x):
    n = (math.sqrt((24 * x) + 1) + 1) / 6
    if round(n) == n:
        return n
    else:
        return False


def solve():
    raise NotImplementedError


if __name__ == '__main__':
    print(solve())
