import time
import primes

start_time = time.clock()

upper_bound = 1000000

prime_list = primes.find_primes_less_than_n(upper_bound)

primes_time = time.clock()
print('Primes Generated. Elapsed Time: ' + str(primes_time - start_time))

last_index = upper_bound - 1

for i in prime_list:
    if i > upper_bound / 2:
        last_index = prime_list.index(i)
        # print(last_index, i)
        break

prime_sums = dict()

for i in prime_list[1:last_index]:
    # print(i)
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

print(max_key, prime_sums[max_key])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
