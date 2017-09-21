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


def solve():
    nums = [i for i in fib_list(4000000) if i % 2 == 0]
    return sum(nums)
