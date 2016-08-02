import time


start_time = time.clock()

file = open('022_names.txt', 'r')

print(sum([(count + 1) * sum([(ord(i) - 96) for i in name]) for (count, name) in enumerate(sorted(file.read().replace('"', '').lower().split(',')))]))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
