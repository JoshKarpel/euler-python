from math import sqrt

from problems import mymath


def t_from_p(p):
    """Quadratic formula!"""
    return (-1 + sqrt(1 - (4 * (-3 * (p ** 2) + p)))) / 2


def h_from_p(p):
    """Quadratic formula!"""
    return (2 + sqrt(4 - 16 * (-3 * (p ** 2) + p))) / 8


def solve():
    p = 165
    while True:

        p += 1

        t = t_from_p(p)
        if t != int(t):
            continue

        h = h_from_p(p)
        if h != int(h):
            continue

        return mymath.pentagon_number(p)


if __name__ == '__main__':
    print(solve())
