import time
import math


start_time = time.clock()

with open('099_pairs.txt') as file:
    pairs = [[int(x) for x in line.strip('\n').split(',')] for line in file]

print(pairs)

log_values = [pair[1] * math.log(pair[0]) for pair in pairs]

print(max(log_values), log_values.index(max(log_values)) + 1)

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))