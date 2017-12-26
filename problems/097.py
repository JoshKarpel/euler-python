def truncated_double(x, truncate = 20):
    return int(str(2 * x)[-truncate:])


def solve():
    x = 28433

    for i in range(7830457):
        x = truncated_double(x)

    x += 1

    last_ten = str(x)[-10:]
    return last_ten


if __name__ == '__main__':
    print(solve())
