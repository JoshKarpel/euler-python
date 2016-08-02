import time
import miscmath
import math
from fractions import Fraction


start_time = time.clock()

max_denominator = 12000

lower = 1 / 3
upper = 1 / 2

# fractions_list = sorted(list(set([Fraction(n, d) for d in range(2, max_denominator + 1) for n in range(1, d) if lower < n / d < upper])))
# print(len(fractions_list))

fractions_list = set([Fraction(n, d) for d in range(2, max_denominator + 1) for n in range(math.floor(d / 3) - 1, math.ceil(d / 2) + 1) if lower < n / d < upper])
print(len(fractions_list))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
