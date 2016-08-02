import time

start_time = time.clock()

nums = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
print(nums)
print(sum(nums))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time-start_time))
