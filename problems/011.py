import itertools

from . import mymath


def get_grid():
    grid = []
    with open('problems/011_grid.txt', mode = 'r') as f:
        for row_str in f:
            row = [int(x) for x in row_str.split(' ')]
            grid.append(row)

    return grid


SHIFTS = {
    'plus': (0, 1, 2, 3),
    'none': (0, 0, 0, 0),
    'minus': (0, -1, -2, -3),
}


def get_product(grid, row, column, row_shift, column_shift):
    if row_shift == column_shift == 'none':
        return 0

    try:
        return mymath.list_product(grid[row + row_shift][column + col_shift] for row_shift, col_shift in zip(SHIFTS[row_shift], SHIFTS[column_shift]))
    except IndexError:
        return 0


def solve():
    grid = get_grid()
    return max(get_product(grid, r, c, r_shift, c_shift) for r, c, r_shift, c_shift in itertools.product(range(20), range(20), SHIFTS.keys(), SHIFTS.keys()))
