def sum_of_squares(n):
    return int(n * (n + 1) * (2 * n + 1) / 6)


def square_of_sums(n):
    return int((n * (n + 1) / 2) ** 2)


def solve():
    n = 100
    return abs(sum_of_squares(n) - square_of_sums(n))


if __name__ == '__main__':
    print(solve())
