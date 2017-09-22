from . import miscmath


def solve():
    test = 500

    while True:
        test += 1
        triangle = int(test * (test + 1) / 2)
        if len(miscmath.full_factorization(triangle)) > 500:
            return triangle
