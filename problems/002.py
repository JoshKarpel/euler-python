import time


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


def fib_list(limit):
    fibs = [1, 2]
    while True:
        next_term = fibs[-1] + fibs[-2]
        if next_term > limit:
            break
        fibs.append(next_term)
    return fibs


start_time = time.clock()

nums = [i for i in fib_list(4000000) if i % 2 == 0]
# for i in range(10): print(nums[i])
print(sum(nums))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
