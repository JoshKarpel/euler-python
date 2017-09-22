from . import primes


def solve():
    return sum(primes.find_primes_less_than_n(2000000))
