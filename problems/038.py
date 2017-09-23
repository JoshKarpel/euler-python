from problems import mymath


def concatenated_product(integer, list_of_integers):
    return ''.join([str(integer * n) for n in list_of_integers])


def solve():
    concatenated_products = dict()

    upper_bound = 1000000

    digits_sorted = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for test in range(2, upper_bound):
        n = 1
        product = ''
        list_of_ints = []
        while len(product) < 9:
            n += 1
            list_of_ints = list(range(1, n))
            product = concatenated_product(test, list_of_ints)
        if sorted(product) == digits_sorted:
            concatenated_products[(test, len(list_of_ints))] = int(product)

    max_key = mymath.key_of_max_value(concatenated_products)

    return max_key


if __name__ == '__main__':
    print(solve())
