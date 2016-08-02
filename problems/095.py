import time
import miscmath
import utils


@utils.Memoize
def sum_proper_factors(n):
    return sum(miscmath.proper_factorization(n))


# sum_proper_factors = utils.Memoize(sum_proper_factors)

start_time = time.clock()

upper_bound = 1000000

chains = dict()

for start_number in range(1, upper_bound):
    # print(start_number)
    chain = [start_number]
    current_number = sum_proper_factors(start_number)
    while current_number != start_number:
        if current_number > upper_bound or current_number == 0 or len(chain) > 100:
            break
        elif current_number in chains:
            chain += chains[current_number]
            break
        else:
            chain.append(current_number)
            current_number = sum_proper_factors(current_number)
    # print(chain)
    if current_number == start_number:
        chains[start_number] = chain

# print(chains)

# print(chains[12496])
# print(len(chains[12496]))

chain_lengths = {i: len(chains[i]) for i in chains}

max_key = miscmath.key_of_max_value(chain_lengths)

print(max_key, chain_lengths[max_key], chains[max_key])
print(min(chains[max_key]))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
