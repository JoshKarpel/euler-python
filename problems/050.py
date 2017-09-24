from problems import primes


def solve():
    upper_bound = 1000000

    prime_list = primes.find_primes_less_than_n(upper_bound)

    last_index = upper_bound - 1

    for i in prime_list:
        if i > upper_bound / 2:
            last_index = prime_list.index(i)
            break

    prime_sums = dict()

    for i in prime_list[1:last_index]:
        test = -1
        start_index = prime_list.index(i)
        while True:
            test += 2
            current_list = prime_list[start_index:start_index + test]
            current_sum = sum(current_list)
            if current_sum > upper_bound:
                break
            elif current_sum in prime_list:
                prime_sums[i] = (len(current_list), current_sum)

    max_key = max(prime_sums, key = prime_sums.get)

    return max_key


if __name__ == '__main__':
    print(solve())
