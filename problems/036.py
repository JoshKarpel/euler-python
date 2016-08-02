import time
import miscmath

start_time = time.clock()

palindromes = []

for test in range(1, 1000001):
	if miscmath.is_palindrome(test) and miscmath.is_palindrome(miscmath.decimal_to_binary(test)):
		palindromes.append(test)

print(palindromes)
print(sum(palindromes))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))