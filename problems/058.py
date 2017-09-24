from problems import primes


def solve():
    diagonals = [1]
    spiral_depth = 3

    diag_count = 1
    prime_count = 0

    while spiral_depth <= 100000:
        last_number = diagonals[-1]
        for n in range(1, 5):
            diag_count += 1
            diag = last_number + (n * (spiral_depth - 1))
            diagonals.append(diag)
            if primes.is_prime(diag):
                prime_count += 1
            if prime_count / diag_count < .10:
                return spiral_depth
        spiral_depth += 2


if __name__ == '__main__':
    print(solve())
