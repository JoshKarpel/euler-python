from math import ceil, sqrt

from problems import primes


def solve():
    upper_bound = 10000

    odds = [odd for odd in range(3, upper_bound + 1, 2)]
    squares = [2 * (num ** 2) for num in range(int(ceil(sqrt(upper_bound / 2))))]

    prime_list = primes.find_primes_less_than_n(upper_bound)

    for odd in odds:
        for prime in prime_list:
            if odd - prime in squares:
                break
        else:  # loop did not break
            return odd


if __name__ == '__main__':
    print(solve())
