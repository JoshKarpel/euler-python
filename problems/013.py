import os

filepath = os.path.join(os.path.dirname(__file__), '022_names.txt')

def solve():
    with open(filepath) as f:
        numbers = [int(x) for x in f]

    return str(sum(numbers))[:10]
