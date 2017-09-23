from collections import defaultdict


def solve():
    triplet_counts = defaultdict(int)

    for perimeter in range(3, 1001):
        for a in range(1, perimeter):
            for b in range(1, perimeter - a):
                c = perimeter - a - b
                if a ** 2 + b ** 2 == c ** 2:
                    triplet_counts[perimeter] += 1

    return max(triplet_counts, key = triplet_counts.get)


if __name__ == '__main__':
    print(solve())
