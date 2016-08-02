import time
import math

factorials = {i: math.factorial(i) for i in range(0, 10)}


def sum_digit_factorial(n):
    return sum([factorials[(int(i))] for i in str(n)])


start_time = time.clock()

upper_bound = 1000000

# print(sum_digit_factorial(145))

chains = dict()

for start_number in range(1, upper_bound):
    # print(start_number)
    chain = [start_number]
    current = sum_digit_factorial(start_number)
    while current not in chain:
        if current in chains:
            chain += chains[current]
            break
        else:
            chain.append(current)
            current = sum_digit_factorial(current)
    # print(chain)
    chains[start_number] = chain

# print(chains)

# print(chains[69])
# print(len(chains[69]))

sixty_terms = [i for i in chains if len(chains[i]) == 60]

# print(sixty_terms)
print(len(sixty_terms))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
