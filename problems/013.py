import os


def solve():
    filepath = os.path.join(os.path.dirname(__file__), '013_numbers.txt')
    with open(filepath) as f:
        numbers = [int(x) for x in f]

    return int(str(sum(numbers))[:10])


if __name__ == '__main__':
    print(solve())
