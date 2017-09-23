from . import mymath


def solve():
    test = 500

    while True:
        test += 1
        triangle = int(test * (test + 1) / 2)
        if len(mymath.full_factorization(triangle)) > 500:
            return triangle
