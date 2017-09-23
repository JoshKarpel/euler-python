from problems import primes


def solve():
    factors = primes.prime_factorization(600851475143)
    return max(factors)


if __name__ == '__main__':
    print(solve())
