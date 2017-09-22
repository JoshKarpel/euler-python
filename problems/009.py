def solve():
    target = 1000

    for a in range(1, target):
        for b in range(1, target - a):
            c = target - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
