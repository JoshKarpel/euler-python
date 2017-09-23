def digit_power_sum(n, power):
    return sum(int(i) ** power for i in str(n))


def solve():
    upper_bound = 999999
    return sum(x for x in range(2, upper_bound + 1) if x == digit_power_sum(x, 5))


if __name__ == '__main__':
    print(solve())
