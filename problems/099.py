import os
from math import log


def solve():
    filepath = os.path.join(os.path.dirname(__file__), '099_pairs.txt')
    with open(filepath) as file:
        pairs = [[int(x) for x in line.strip('\n').split(',')] for line in file]

    log_values = [pair[1] * log(pair[0]) for pair in pairs]

    return max(log_values), log_values.index(max(log_values)) + 1


if __name__ == '__main__':
    print(solve())
