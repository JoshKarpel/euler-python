from problems import primes


def period(d):
    """Returns the length of the longest recurring cycle in the fraction 1/d."""
    test = 0
    while True:
        test += 1
        if (10 ** test) % d == 1:
            return test


def solve():
    periods_to_d = {}
    for d in primes.find_primes_less_than_n(1000)[4:]:
        periods_to_d[period(d)] = d

    return periods_to_d[max(periods_to_d)]


if __name__ == '__main__':
    print(solve())
