from problems import utils


@utils.memoize
def square_digits(n):
    return sum([int(x) ** 2 for x in str(n)])


def solve():
    upper_bound = 1000000

    sums = {1: 0, 89: 0}
    chains = {}

    for test in range(1, upper_bound + 1):
        # print(test)
        current_test = test
        while True:
            if current_test == 1:
                sums[1] += 1
                chains[test] = 1
                break
            elif current_test == 89:
                sums[89] += 1
                chains[test] = 89
                break
            elif current_test in chains:
                chains[test] = chains[current_test]
                sums[chains[test]] += 1
                break
            current_test = square_digits(current_test)

    return sums


if __name__ == '__main__':
    print(solve())
