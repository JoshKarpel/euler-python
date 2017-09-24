from problems import utils, mymath


@utils.memoize
def sum_proper_factors(n):
    return sum(mymath.proper_factorization(n))


def solve():
    upper_bound = 1000000

    chains = dict()

    for start_number in range(1, upper_bound):
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
        if current_number == start_number:
            chains[start_number] = chain

    chain_lengths = {i: len(chains[i]) for i in chains}

    max_key = mymath.key_of_max_value(chain_lengths)

    return min(chains[max_key])


if __name__ == '__main__':
    print(solve())
