import time


def same_digits(n, m):
    for i in str(n):
        if i not in str(m):
            return False
    for j in str(m):
        if j not in str(n):
            return False
    return True


start_time = time.clock()

x = 0

while True:
    x += 1
    if same_digits(x, 2 * x) and same_digits(x, 3 * x) and same_digits(x, 4 * x) and same_digits(x, 5 * x) and same_digits(x, 6 * x):
        print(x, 2 * x, 3 * x, 4 * x, 5 * x, 6 * x)
        break

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
