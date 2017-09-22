from math import sqrt, ceil


def d(n):
    factors = set()
    for divisor in range(2, int(ceil(sqrt(n)))):
        if n % divisor == 0:
            factors.add(divisor)
            factors.add(int(n / divisor))
    return sum(factors) + 1


def solve():
    lim = 10001

    num_to_factors = {n: d(n) for n in range(lim)}

    amicable_numbers = set()
    for a in range(lim):
        for b in range(a + 1, lim):
            if num_to_factors[a] == b and num_to_factors[b] == a:
                amicable_numbers.add(a)
                amicable_numbers.add(b)

    return sum(amicable_numbers)
