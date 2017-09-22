from collections import defaultdict, Counter

from . import primes


def merge_counts_by_cmp(*counters, cmp = max):
    keys = set(sum((list(counter.keys()) for counter in counters), list()))
    merged = Counter()
    for counter in counters:
        for key in keys:
            merged[key] = cmp(merged[key], counter[key])
    return merged


def multiply_counter(counter):
    acc = 1
    for factor, count in counter.items():
        acc *= factor ** count

    return acc


def solve():
    factorizations = [primes.prime_factorization(n) for n in range(2, 21)]
    factor_counts = [Counter(factorization) for factorization in factorizations]

    max_counts = merge_counts_by_cmp(*factor_counts, cmp = max)

    return multiply_counter(max_counts)
