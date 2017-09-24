import os
import itertools

from problems import mymath


def solve():
    filepath = os.path.join(os.path.dirname(__file__), '067_triangle.txt')
    with open(filepath) as file:
        words = [word for word in file.read().replace('"', '').lower().split(',')]

    square_anagrams = dict()

    for word in words:
        square_anagrams[word] = []
        for anagram in itertools.permutations(word):
            anagram_number = int(''.join([str(ord(letter) - 96) for letter in anagram]))
            if mymath.is_square(anagram_number) and not mymath.is_palindrome(anagram):
                square_anagrams[word] += (anagram, anagram_number)

    return square_anagrams


if __name__ == '__main__':
    print(solve())
