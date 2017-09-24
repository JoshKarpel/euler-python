import math

factorials = {i: math.factorial(i) for i in range(0, 10)}


def sum_digit_factorial(n):
    return sum([factorials[(int(i))] for i in str(n)])


def solve():
    upper_bound = 1000000

    chains = dict()

    for start_number in range(1, upper_bound):
        chain = [start_number]
        current = sum_digit_factorial(start_number)
        while current not in chain:
            if current in chains:
                chain += chains[current]
                break
            else:
                chain.append(current)
                current = sum_digit_factorial(current)
        chains[start_number] = chain

    sixty_terms = [i for i in chains if len(chains[i]) == 60]

    return len(sixty_terms)


if __name__ == '__main__':
    print(solve())
