import itertools

from problems import primes


def solve():
    upper_bound = 10000

    primes_list = set(n for n in primes.find_primes_less_than_n(upper_bound) if len(str(n)) == 4)

    permutations = {}

    for prime in primes_list:
        permutations[prime] = set(p for p in [int(''.join(p)) for p in itertools.permutations(str(prime))] if p in primes_list)

        if len(permutations[prime]) < 3:
            del permutations[prime]

    for p, s in permutations.items():
        for permutation in itertools.permutations(s, r = 3):
            sort = sorted(permutation)
            if sort[2] - sort[1] == sort[1] - sort[0]:
                print(sort[2] - sort[1])
                print(sort)


if __name__ == '__main__':
    print(solve())
