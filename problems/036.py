from problems import mymath


def solve():
    palindromes = []

    for test in range(1, 1000001):
        if mymath.is_palindrome(test) and mymath.is_palindrome(mymath.decimal_to_binary(test)):
            palindromes.append(test)

    return sum(palindromes)


if __name__ == '__main__':
    print(solve())
