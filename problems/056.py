from problems import mymath


def digit_sum(n):
    return sum([int(i) for i in str(n)])


def solve():
    digit_sums = dict()

    for a in range(1, 101):
        for b in range(1, 101):
            digit_sums[(a, b)] = digit_sum(a ** b)

    max_key = mymath.key_of_max_value(digit_sums)

    return max_key


if __name__ == '__main__':
    print(solve())
