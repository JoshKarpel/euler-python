import time
from problems import utils
import math
import miscmath

@utils.Memoize
def pentagon(n):
    return int(n * ((3 * n) - 1) / 2)

@utils.Memoize
def is_pentagon(x):
    n = (math.sqrt((24 * x) + 1) + 1) / 6
    if round(n) == n:
        return n
    else:
        return False

start_time = time.clock()



end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))