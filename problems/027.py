from problems import primes


def solve():
    longest = [0, 0, 0]

    primes_list = primes.find_primes_less_than_n(1000)

    for b in range(-999, 1000, 2):
        for c in primes_list:
            n = -1
            while True:
                n += 1
                q = n ** 2 + (b * n) + c
                if not primes.is_prime(q) or q <= 1:
                    if n > longest[2]:
                        longest = [b, c, n, q]
                    break

    return longest[0] * longest[1]


if __name__ == '__main__':
    print(solve())
