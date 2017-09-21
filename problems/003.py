from . import primes


def solve():
    factors = primes.prime_factorization(600851475143)
    return max(factors)
