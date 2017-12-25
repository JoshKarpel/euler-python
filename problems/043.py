import itertools

from problems import mymath, primes

divisors = primes.find_n_primes(10)


def divisibility_test(n):
    n_str = str(n)
    numerators = [int(n_str[i:i + 3]) for i in range(1, 8)]
    return all(num % div == 0 for num, div in zip(numerators, divisors))


def solve():
    permutations = (int(''.join(i)) for i in itertools.permutations('0123456789'))

    numbers = []

    for test in permutations:
        if test < 1000000:  # must have started with a zero
            continue

        if divisibility_test(test):
            numbers.append(test)

    return sum(numbers)


if __name__ == '__main__':
    print(solve())
