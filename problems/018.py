import time

with open('018_triangle.txt') as file:
    triangle = [[int(x) for x in line.strip('\n').split(' ')] for line in file]

start_time = time.clock()

# print(triangle)

current_sum_row = triangle[-1]
for row in reversed(triangle[0:-1]):
    current_sum_row = [row[i] + max(current_sum_row[i], current_sum_row[i + 1]) for i in range(len(row))]
    print(current_sum_row)

print('MAXIMUM SUM: ', current_sum_row[0])

end_time = time.clock()

# print(triangle)

print('Elapsed Time: ' + str(end_time - start_time))