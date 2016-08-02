import time
import miscmath

start_time = time.clock()

file = open('098_words.txt', 'r')

words = [word for word in file.read().replace('"', '').lower().split(',')]

# words = ['ability']

square_anagrams = dict()

for word in words:
    print(word)
    square_anagrams[word] = []
    for anagram in miscmath.permutations(word):
        anagram_number = int(''.join([str(ord(letter) - 96) for letter in anagram]))
        # print(anagram, anagram_number)
        if miscmath.is_square(anagram_number) and not miscmath.is_palindrome(anagram):
            square_anagrams[word] += (anagram, anagram_number)
            print(True)
            print(square_anagrams)

print(square_anagrams)

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
