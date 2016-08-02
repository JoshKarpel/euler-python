import time

start_time = time.clock()

print(sum([int(i) for i in str(2 ** 1000)]))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
