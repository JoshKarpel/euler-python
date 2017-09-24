digits = '123456789'


def is_pandigital(x):
    return ''.join(sorted(x)) == digits


def solve():
    upper_bound = 1000000
    k = 2
    fib = [1, 1]

    while True:
        k += 1
        # print(k)
        fib.append(fib[-1] + fib[-2])
        s = str(fib[-1])
        if is_pandigital(s[0:9]) and is_pandigital(s[-9:]):
            return k


if __name__ == '__main__':
    print(solve())
