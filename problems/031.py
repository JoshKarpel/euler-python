from problems import mymath

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


# see https://en.wikipedia.org/wiki/Partition_(number_theory)
def solve():
    series_list = [
        mymath.GeometricSeries({power: 1 for power in range(0, 201, k)})
        for k in COINS
    ]

    result = mymath.iterable_product(series_list, initial = mymath.GeometricSeries.one())

    return result[200]


if __name__ == '__main__':
    print(solve())
