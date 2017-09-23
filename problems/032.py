import itertools

from problems import mymath


def solve():
    digits_sorted = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    permutations = itertools.permutations(digits_sorted)

    correct_products = set()

    for digit_string in permutations:
        for i in range(1, 5):
            if int(''.join(digit_string[0:i])) * int(''.join(digit_string[i:5])) == int(''.join(digit_string[5:])):
                correct_products.add(int(''.join(digit_string[5:])))

    return sum(correct_products)


if __name__ == '__main__':
    print(solve())
