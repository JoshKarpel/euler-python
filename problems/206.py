import re
from math import sqrt


def solve():
    base = '1234567890'
    target = re.compile('1.2.3.4.5.6.7.8.9.0')

    lower_bound = int(round(sqrt(1020304050607080900), -1))
    upper_bound = int(round(sqrt(1929394959697989990), -1)) + 10

    lower_bound += 20

    test = lower_bound
    while test < upper_bound:
        # print(test, test ** 2, (test - lower_bound) / (upper_bound - lower_bound))
        if target.match(str(test ** 2)) is not None:
            return test
        test += 40
        # print(test, test ** 2, (test - lower_bound) / (upper_bound - lower_bound))
        if target.match(str(test ** 2)) is not None:
            return test
        test += 60


if __name__ == '__main__':
    print(solve())
