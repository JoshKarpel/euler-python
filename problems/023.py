import time
import miscmath


def abundant_number_test(n):
    if sum(miscmath.proper_factorization(n)) > n:
        return True
    else:
        return False


start_time = time.clock()

upper_bound = 28123

abundant_numbers = set()

for test in range(1, upper_bound + 1):
    if abundant_number_test(test):
        abundant_numbers.add(test)

print(len(abundant_numbers))

abundant_numbers_time = time.clock()

print('Abundant Numbers Generated. Elapsed Time: ' + str(abundant_numbers_time - start_time))

abundant_sums = {i + j for i in abundant_numbers for j in abundant_numbers}

print(len(abundant_sums))

abundant_sums_time = time.clock()

print('Abundant Sums Generated. Elapsed Time: ' + str(abundant_sums_time - start_time))

nums = set(range(1, upper_bound + 1)).difference(abundant_sums)

# print(abundant_numbers)
# print(abundant_sums)
print(sorted(nums))
print(sum(nums))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
