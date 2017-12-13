import itertools
from math import ceil

from problems import mymath


def solve():
    numerators = range(10, 100)
    denominators = range(10, 100)
    fractions = []

    for numerator in numerators:
        for denominator in denominators:
            if denominator > numerator:
                fractions.append([numerator, denominator])

    answers = []

    for fraction in fractions:
        numerator_str = str(fraction[0])
        denominator_str = str(fraction[1])
        for i in numerator_str:
            if i == str(0):
                break
            elif i in denominator_str:
                numerator_str_cancelled = numerator_str.replace(i, '', 1)
                denominator_str_cancelled = denominator_str.replace(i, '', 1)
                if denominator_str_cancelled != str(0) and int(numerator_str_cancelled) / int(denominator_str_cancelled) == fraction[0] / fraction[1]:
                    answers.append(fraction[0] / fraction[1])

    return int(ceil(1 / mymath.iterable_product(answers)))


if __name__ == '__main__':
    print(solve())
