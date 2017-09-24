def solve():
    nth_powers = [(i, j, i ** j, len(str(i ** j))) for j in range(1, 50) for i in range(2, 10)]

    total = 0
    for i in nth_powers:
        if i[1] == i[3]:
            total += 1

    return total + 1
