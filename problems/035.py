from problems import primes


def generate_rotations(n):
    n_str = str(n)
    digit_count = len(n_str)
    rotations = []
    for i in range(digit_count):
        rotations.append(int(n_str[i:] + n_str[:i]))
    return set(rotations)


def strip_primes(n):
    n_str = str(n)
    if '0' in n_str or '2' in n_str or '4' in n_str or '6' in n_str or '8' in n_str:
        return False
    else:
        return True


def solve():
    upper_bound = 1000000

    primes_list = primes.find_primes_less_than_n(upper_bound)
    stripped_primes_list = [2] + [prime for prime in primes_list if strip_primes(prime)]

    circular_primes = []

    for prime in stripped_primes_list:
        if prime not in circular_primes:
            for rotated_prime in generate_rotations(prime):
                if rotated_prime not in stripped_primes_list:
                    break  # if prime is not circular, break for loop
            else:  # if loop does not break, the prime is circular
                circular_primes += generate_rotations(prime)

    return len(circular_primes)


if __name__ == '__main__':
    print(solve())
