from math import ceil, sqrt, log

golden_ratio = (1 + sqrt(5)) / 2


def solve():
    """Approximate F_n using phi^n / sqrt(5) and do some algebra to find n."""
    return ceil((999 * log(10, golden_ratio)) + log(sqrt(5), golden_ratio))


if __name__ == '__main__':
    print(solve())
