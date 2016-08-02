import time
import miscmath
from fractions import Fraction


start_time = time.clock()

# write recursively
# ie
# 10 > 7+3 or 5+5
# 7+3 is done
# 5+5 -> 3 + 2 + 5
# 3+ 2 + 5 -> 3 + 2 + 3 + 2 is done
# if the number youre breaking is even you get 2 initially, if its odd you get 1 more sum

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))