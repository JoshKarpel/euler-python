import itertools


def solve():
    upper_bound = 1000

    permutations_set = dict()
    permutations_included = []
    cubes = {str(i ** 3) for i in range(1, upper_bound)}

    for test_index in range(1, upper_bound):
        test_cube = test_index ** 3
        intersect = set(itertools.permutations(str(test_cube))).intersection(cubes)
        if len(intersect) == 5:
            break


if __name__ == '__main__':
    print(solve())
