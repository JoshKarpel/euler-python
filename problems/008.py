import os

from problems import mymath


def solve():
    filepath = os.path.join(os.path.dirname(__file__), '008_number.txt')
    with open(filepath) as f:
        number = f.read().replace('\n', '')

    numbers = [int(x) for x in number]

    largest_product = max(mymath.iterable_product(numbers[start: start + 13]) for start in range(len(numbers) - 13))

    return largest_product


if __name__ == '__main__':
    print(solve())
