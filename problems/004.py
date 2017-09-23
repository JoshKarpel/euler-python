def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


def solve():
    products = []

    for i in range(100, 1000):
        for j in range(i, 1000):
            products.append(i * j)

    products = sorted((i * j for i in range(100, 1000) for j in range(i, 1000)), reverse = True)
    for p in products:
        if is_palindrome(p):
            return p


if __name__ == '__main__':
    print(solve())
