import time
import miscmath
import math
from fractions import Fraction


start_time = time.clock()

max_denominator = 1000000

lower = 428571 / 1000000
upper = 3 / 7

fractions_list = sorted(list(set([Fraction(n, d) for d in range(700000, max_denominator + 1) for n in range(428400, math.ceil(3 * d / 7)) if lower <= n / d < upper])))

print(len(fractions_list))

# print(fractions_list.index(Fraction(3, 7)))
# print(fractions_list[fractions_list.index(Fraction(3, 7)) - 1])

print(fractions_list[-1])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
