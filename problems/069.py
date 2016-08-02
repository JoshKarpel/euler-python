import time
import primes
import miscmath

start_time = time.clock()

upper_bound = 1000001

prime_list = primes.find_primes_less_than_n(upper_bound)

primes_time = time.clock()

print('Primes generated. Elapsed Time: ' + str(primes_time - start_time))

divisors = dict(zip(range(upper_bound), prime_list))

prime_factorization_dictionary = dict()


def prime_factorization_specialized(n):
    if n in prime_list:
        return [n]
    factors = []
    divisor_key = 0
    while n != 1:
        divisor = divisors[divisor_key]
        if n in prime_factorization_dictionary:
            factors += prime_factorization_dictionary[n]
            break
        elif n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor_key += 1
    return factors


for n in range(2, upper_bound):
    prime_factorization_dictionary[n] = prime_factorization_specialized(n)

# print(prime_factorization_dictionary)

factorizations_time = time.clock()

print('Prime Factorization Dictionary Generated. Elapsed Time: ' + str(factorizations_time - start_time))


def phi(n):
    return round(n * miscmath.list_product([1 - (1 / p) for p in set(prime_factorization_dictionary[n])]))


ratios = {i: i / phi(i) for i in range(2, upper_bound)}

max_key = miscmath.key_of_max_value(ratios)

# print(ratios)

print(max_key, ratios[max_key])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
