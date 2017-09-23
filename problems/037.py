from problems import primes


def is_truncatable(p, prime_list):
    p_str = str(p)

    for trunc in range(len(p_str) - 1):
        if int(p_str[:trunc + 1]) not in prime_list or int(p_str[trunc + 1:]) not in prime_list:
            return False

    return True


def solve():
    truncatabale_primes = []
    prime_list = []

    for p in primes.generate_primes():
        prime_list.append(p)

        if p < 10:
            continue

        if len(truncatabale_primes) == 11:
            break

        if is_truncatable(p, prime_list):
            truncatabale_primes.append(p)

    return sum(truncatabale_primes)


if __name__ == '__main__':
    print(solve())
