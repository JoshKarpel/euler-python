import math
from collections import defaultdict


def iterable_product(iterable, initial = 1):
    product = initial
    for element in iterable:
        product *= element
    return product


def elementwise_multiply(list_a, list_b):
    return [a * b for a, b in zip(list_a, list_b)]


def elementwise_sum(list_a, list_b):
    return [a + b for a, b in zip(list_a, list_b)]


def sum_of_squares(n):
    return int(n * (n + 1) * (2 * n + 1) / 6)


def square_of_sums(n):
    return int((n * (n + 1) / 2) ** 2)


def full_factorization(n):
    factors = set()
    for d in range(1, int(math.ceil(math.sqrt(n)) + 1)):
        if n % d == 0 and d not in factors:
            factors.add(d)
            factors.add(int(n / d))
    return sorted(factors)


def proper_factorization(n):
    return full_factorization(n)[:-1]


def quadratic_formula(a, b, c):
    sqrt_disc = math.sqrt(b ** 2 - 4 * a * c)
    return (-b + sqrt_disc) / (2 * a), (-b - sqrt_disc) / (2 * a)


def key_of_max_value(dictionary):
    return max(dictionary, key = dictionary.get)


def key_of_min_value(dictionary):
    return min(dictionary, key = dictionary.get)


def is_square(n):
    sqrt_n = math.sqrt(n)
    return sqrt_n == int(sqrt_n)


def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


def decimal_to_binary(n):
    return int(bin(n)[2:])


def number_of_combinations(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def triangle_number(n):
    return int(n * (n + 1) / 2)


def pentagon_number(n):
    return int(n * ((3 * n) - 1) / 2)


def hexagon_number(n):
    return int(n * ((2 * n) - 1))


class GeometricSeries(defaultdict):
    def __init__(self, *args, **kwargs):
        super().__init__(int, *args, **kwargs)

    def __mul__(self, other, truncate = None):
        result = GeometricSeries()

        for power_self, coefficient_self in self.items():
            for power_other, coefficient_other in other.items():
                if truncate is not None and power_self + power_other > truncate:
                    continue

                result[power_self + power_other] += coefficient_self * coefficient_other

        return result

    def multiply(self, other, truncate = None):
        return self.__mul__(other, truncate = truncate)

    def __str__(self):
        return ' + '.join(f'{coefficient if coefficient != 1 else ""}x^{power}' for power, coefficient in sorted(self.items()))

    @classmethod
    def one(cls):
        """Return the GeometricSeries representation of the identity."""
        return cls({0: 1})
