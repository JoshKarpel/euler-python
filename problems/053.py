from problems import mymath


def solve():
    combination_values = []

    for n in range(1, 101):
        for r in range(0, n + 1):
            combination_values.append(mymath.number_of_combinations(n, r))
    target = list(i for i in combination_values if i > 1000000)

    return sum(i > 1000000 for i in combination_values)


if __name__ == '__main__':
    print(solve())
