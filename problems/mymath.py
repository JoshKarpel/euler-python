import math


def list_product(num_list):
    product = 1
    for i in num_list:
        product *= i
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
    factors = set()
    for divisor in range(1, int(math.ceil(math.sqrt(n)) + 1)):
        if n % divisor == 0:
            factors.add(divisor)
            factors.add(round((n / divisor)))
    return sorted(factors)[:-1]


def quadratic_formula(a, b, c):
    sqrt_disc = math.sqrt(b ** 2 - 4 * a * c)
    return (-b + sqrt_disc) / (2 * a), (-b - sqrt_disc) / (2 * a)


def key_of_max_value(dictionary):
    return max(dictionary, key = dictionary.get)


def key_of_min_value(dictionary):
    return min(dictionary, key = dictionary.get)


def is_square(n):
    sqrt_n = math.sqrt(n)
    if sqrt_n == math.floor(sqrt_n):
        return True
    return False


def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


def decimal_to_binary(n):
    return int(bin(n)[2:])


def n_choose_r(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def triangle_number(n):
    return int(n * (n + 1) / 2)


def pentagon_number(n):
    return int(n * ((3 * n) - 1) / 2)


def hexagon_number(n):
    return int(n * ((2 * n) - 1))
