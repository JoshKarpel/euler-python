from problems import primes


def solve():
    return primes.find_n_primes(10001)[-1]


if __name__ == '__main__':
    print(solve())
