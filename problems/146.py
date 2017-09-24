from problems import primes


def solve():
    upper_bound = 10 ** 7
    primes_list = primes.find_primes_less_than_n(upper_bound)

    return len(primes_list)


if __name__ == '__main__':
    print(solve())
