import time
import math
import itertools as it
import miscmath
import re

base = '1234567890'
target = re.compile('1.2.3.4.5.6.7.8.9.0')


lower_bound = int(round(math.sqrt(1020304050607080900), -1))
upper_bound = int(round(math.sqrt(1929394959697989990), -1)) + 10

lower_bound += 20

print(lower_bound)

print((upper_bound - lower_bound) / 10)

start_time = time.clock()

# for x in range(0, 500, 10):
#     print(x, x ** 2)

test = lower_bound
while test < upper_bound:
    # print(test, test ** 2, (test - lower_bound) / (upper_bound - lower_bound))
    if target.match(str(test ** 2)) is not None:
        print('FOUND IT: ', test, test ** 2)
        break
    test += 40
    # print(test, test ** 2, (test - lower_bound) / (upper_bound - lower_bound))
    if target.match(str(test ** 2)) is not None:
        print('FOUND IT: ', test, test ** 2)
        break
    test += 60


end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))