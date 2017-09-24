import os


def solve():
    filepath = os.path.join(os.path.dirname(__file__), '067_triangle.txt')
    with open(filepath) as file:
        triangle = [[int(x) for x in line.strip('\n').split(' ')] for line in file]

    current_sum_row = triangle[-1]
    for row in reversed(triangle[0:-1]):
        current_sum_row = [row[i] + max(current_sum_row[i], current_sum_row[i + 1]) for i in range(len(row))]

    return current_sum_row[0]


if __name__ == '__main__':
    print(solve())
