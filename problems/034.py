import math

digit_factorials = {str(x): math.factorial(x) for x in range(10)}


def digit_factorial_sum(n):
    return sum(digit_factorials[i] for i in str(n))


def solve():
    upper_bound = digit_factorials['9'] * 7
    return sum(x for x in range(3, upper_bound) if x == digit_factorial_sum(x))


if __name__ == '__main__':
    print(solve())
