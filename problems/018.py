def solve():
    with open('problems/018_triangle.txt') as file:
        triangle = [[int(x) for x in line.strip('\n').split(' ')] for line in file]

    current_sum_row = triangle[-1]
    for row in reversed(triangle[0:-1]):
        current_sum_row = [row[i] + max(current_sum_row[i], current_sum_row[i + 1]) for i in range(len(row))]

    return current_sum_row[0]
