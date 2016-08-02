import time
import miscmath
import math
from fractions import Fraction

digits = '123456789'


def is_pandigital(x):
    if ''.join(sorted(x)) == digits:
        return True
    else:
        return False

start_time = time.clock()

upper_bound = 1000000
k = 2
fib = [1, 1]

while True:
    k += 1
    # print(k)
    fib.append(fib[-1] + fib[-2])
    s = str(fib[-1])
    if is_pandigital(s[0:9]) and is_pandigital(s[-9:]):
        print(k, fib[-1])
        break

# is_pandigital('123')

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
