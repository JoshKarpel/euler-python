import math


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for divisor in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def find_n_primes(n):
    primes = [2]
    test = 2
    while len(primes) < n:
        test += 1
        for d in primes:
            if test % d == 0:
                break
            elif d > math.sqrt(test):
                primes.append(test)
                break
    return primes


def find_primes_less_than_n(n):
    primes = [2]
    test = 2
    while test < n:
        test += 1
        for d in primes:
            if test % d == 0:
                break
            elif d > math.sqrt(test):
                primes.append(test)
                break
    return primes


def generate_primes():
    yield 2
    primes = [2]
    test = 2
    while True:
        test += 1
        for d in primes:
            if test % d == 0:
                break
            elif d > math.sqrt(test):
                primes.append(test)
                yield test
                break


def sieve_of_eratosthenes(n):
    primes = []
    not_primes = []
    for test in range(2, n):
        if test not in not_primes:
            primes.append(test)
            i = test
            while i < n:
                i += test
                if test not in not_primes:
                    not_primes.append(i)
        elif test in primes:
            continue
    return primes


def prime_factorization(n):
    factors = []
    divisor = 2
    n_sqrt = math.sqrt(n)
    while True:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        elif n == 1:
            break
        elif divisor > n_sqrt:
            factors.append(int(n))
            break
        else:
            divisor += 1
    return factors


def relatively_prime(n):
    relatives = set()
    relatives.add(1)
    for test in range(2, n):
        if len(set(prime_factorization(n)).intersection(set(prime_factorization(test)))) == 0:
            relatives.add(test)
    return relatives
