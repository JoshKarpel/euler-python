def fibs_to_limit(limit):
    fibs = [1, 1]
    while True:
        next_term = sum(fibs[-2:])
        if next_term > limit:
            break
        fibs.append(next_term)
    return fibs


def solve():
    return sum(i for i in fibs_to_limit(4000000) if i % 2 == 0)


if __name__ == '__main__':
    print(solve())
