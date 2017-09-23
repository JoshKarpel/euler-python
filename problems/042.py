import os


def solve():
    filepath = os.path.join(os.path.dirname(__file__), '042_words.txt')
    with open(filepath) as f:
        word_value_list = (sum([(ord(i) - 96) for i in word]) for word in f.read().replace('"', '').lower().split(','))

    triangle_numbers = [n * (n + 1) / 2 for n in range(1, 1000)]

    return sum(wv in triangle_numbers for wv in word_value_list)


if __name__ == '__main__':
    print(solve())
