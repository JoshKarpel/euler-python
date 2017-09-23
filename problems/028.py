def solve():
    size = 1001

    diagonals = [1]
    spiral_depth = 3

    for spiral_depth in range(3, size + 1, 2):
        last_number = diagonals[-1]
        diagonals += [last_number + (n * (spiral_depth - 1)) for n in range(1, 5)]

    return sum(diagonals)
