import os

from . import mymath

filepath = os.path.join(os.path.dirname(__file__), '022_names.txt')

def solve():
    with open(filepath) as f:
        number = f.read().replace('\n', '')

    numbers = [int(x) for x in number]

    largest_product = max(mymath.list_product(numbers[start: start + 13]) for start in range(len(numbers) - 13))

    return largest_product
