import time
import math


def digit_factorial_sum(n):
    return sum([math.factorial(int(i)) for i in str(n)])


start_time = time.clock()

upper_bound = 9999999

curious = set()

for test in range(3, upper_bound):
    if test == digit_factorial_sum(test):
        curious.add(test)

print(curious)
print(sum(curious))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
