import time


def sum_of_squares(n):
    # return sum([i**2 for i in range(1,n+1)])
    return int(n * (n + 1) * (2 * n + 1) / 6)


def square_of_sums(n):
    # return sum([i for i in range(1,n+1)])**2
    return int((n * (n + 1) / 2) ** 2)


start_time = time.clock()

n = 100

sumSq = sum_of_squares(n)
sqSum = square_of_sums(n)

print(sumSq)
print(sqSum)
print(abs(sumSq - sqSum))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
