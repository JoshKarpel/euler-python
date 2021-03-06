import os



def solve():
    filepath = os.path.join(os.path.dirname(__file__), '022_names.txt')
    with open(filepath, mode = 'r') as f:
        names = f.read().lower().replace('"', '').split(',')

    return sum((pos + 1) * sum(ord(char) - 96 for char in name) for pos, name in enumerate(sorted(names)))


if __name__ == '__main__':
    print(solve())
