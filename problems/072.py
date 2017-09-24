from fractions import Fraction

from problems import primes


def solve():
    max_denominator = 10000

    primes_list = primes.find_primes_less_than_n(max_denominator + 1) + [max_denominator]

    powers_of_two = []
    i = 4
    while i < max_denominator:
        powers_of_two.append(i)
        i += 2

    fractions_set = {Fraction(n, d) for d in primes_list for n in range(1, d)}.union({Fraction(1, d) for d in powers_of_two}).union({Fraction(d - 1, d) for d in powers_of_two})

    return len(fractions_set)

    # should be possible to just count them instead of constructing them by looking at the pattern in the numerators and denominators, constructing backwards from the upper bound


if __name__ == '__main__':
    print(solve())
