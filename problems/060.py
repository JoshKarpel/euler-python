from problems import primes


def solve():
    current_primes = []

    set_size = 0

    for latest_prime in primes.generate_primes():
        if set_size < 4:
            set_size += 1
            current_primes.append(latest_prime)
        else:
            current_primes.pop(0)
            current_primes.append(latest_prime)
            found = True
            for i in range(set_size):
                for j in range(set_size):
                    prime_test = int(''.join([str(current_primes[i]), str(current_primes[j])]))
                    if not primes.is_prime(prime_test):
                        found *= False
            if found:
                return sum(current_primes)


if __name__ == '__main__':
    print(solve())
