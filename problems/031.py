from collections import defaultdict

from problems import mymath


class GeometricSeries(defaultdict):
    def __init__(self, *args, **kwargs):
        super().__init__(int, *args, **kwargs)

    def __mul__(self, other, truncate = None):
        result = GeometricSeries()

        for power_self, coefficient_self in self.items():
            for power_other, coefficient_other in other.items():
                if truncate and power_self + power_other > truncate:
                    continue

                result[power_self + power_other] += coefficient_self * coefficient_other

        return result

    def __str__(self):
        return ' + '.join(f'{coefficient if coefficient != 1 else ""}x^{power}' for power, coefficient in sorted(self.items()))

    @classmethod
    def one(cls):
        """Return the GeometricSeries representation of the identity."""
        return cls({0: 1})


COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def solve():
    series_list = [
        GeometricSeries({power: 1 for power in range(0, 201, k)})
        for k in COINS
    ]

    result = mymath.iterable_product(series_list, initial = GeometricSeries.one())

    return result[200]


if __name__ == '__main__':
    print(solve())
