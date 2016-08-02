import time


start_time = time.clock()

print(sum([i ** i for i in range(1, 1001)]))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))