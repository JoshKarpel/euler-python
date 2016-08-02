import time


start_time = time.clock()

numbers = [int(number) for number in list(open('013_numbers.txt', 'r'))]

print(numbers)

print(str(sum(numbers))[:10])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))