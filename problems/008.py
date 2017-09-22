from . import miscmath


def solve():
    with open('problems/008_number.txt', mode = 'r') as f:
        number = f.read().replace('\n', '')

    numbers = [int(x) for x in number]

    largest_product = max(miscmath.list_product(numbers[start: start + 13]) for start in range(len(numbers) - 13))

    return largest_product
