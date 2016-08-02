import time


def is_bouncy(x):
    x_str = str(x)
    sorted_x_str = ''.join(sorted(x_str))
    if x_str == sorted_x_str or x_str == sorted_x_str[::-1]:
        return False
    else:
        return True


start_time = time.clock()

upper_bound = 10000000
bouncy_count = 0
total = 0

for test in range(1, upper_bound + 1):
    total += 1
    if is_bouncy(test):
        bouncy_count += 1
    # print(test, bouncy_count, bouncy_count / total)
    if bouncy_count / total == .99:
        print(test, bouncy_count, bouncy_count / total)
        break

# print(bouncy_count, bouncy_count / total)

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))