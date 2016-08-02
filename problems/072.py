import time
import miscmath
from fractions import Fraction
import primes


start_time = time.clock()

max_denominator = 10000

primes_list = primes.find_primes_less_than_n(max_denominator + 1) + [max_denominator]
# print(primes_list)
# print(len(primes_list))

powers_of_two = []
i = 4
while i < max_denominator:
    powers_of_two.append(i)
    i += 2

# print(powers_of_two)

# fractions_set = {Fraction(n, d) for d in range(2, max_denominator + 1) for n in range(1, d)}
# print(sorted(fractions_set))
# print(len(sorted(fractions_set)))

fractions_set = {Fraction(n, d) for d in primes_list for n in range(1, d)}.union({Fraction(1, d) for d in powers_of_two}).union({Fraction(d - 1, d) for d in powers_of_two})
# print(sorted(fractions_set))
print(len(fractions_set))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))

# should be possible to just count them instead of constructing them by looking at the pattern in the numerators and denominators, constructing backwards from the upper bound