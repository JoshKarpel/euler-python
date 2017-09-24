def is_bouncy(x):
    x_str = str(x)
    sorted_x_str = ''.join(sorted(x_str))
    return x_str == sorted_x_str or x_str == sorted_x_str[::-1]


def solve():
    upper_bound = 10000000
    bouncy_count = 0
    total = 0

    for test in range(1, upper_bound + 1):
        total += 1
        if is_bouncy(test):
            bouncy_count += 1
        if bouncy_count / total == .99:
            return test


if __name__ == '__main__':
    print(solve())
