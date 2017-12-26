import itertools


def reverse_n(n):
    s_n = str(n)
    rev_s = ''.join(s for s in reversed(s_n))
    return int(rev_s) if rev_s[0] != '0' else None


ODD_DIGITS = list(str(x) for x in range(1, 10) if x % 2 != 0)


def all_digits_odd(str_n):
    return all(s in ODD_DIGITS for s in str_n)


def solve():
    upper_bound = 100_000_000  # it turns out there are no 9-digit reversible numbers!?

    candidates = set()
    for r in range(1, len(str(upper_bound)) + 1):
        new = list(int(''.join(s)) for s in itertools.product(ODD_DIGITS, repeat = r))
        candidates = candidates.union(set(new))

    reversible_count = 0
    for n in range(1, upper_bound):
        r = reverse_n(n)
        try:
            if n + r in candidates:
                reversible_count += 1
        except TypeError:
            pass

    return reversible_count


if __name__ == '__main__':
    print(solve())
