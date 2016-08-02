import time
import miscmath


def concatenated_product(integer, list_of_integers):
	return ''.join([str(integer * n) for n in list_of_integers])

start_time = time.clock()

#print(concatenated_product(192, [1, 2, 3]))
#print(concatenated_product(9, [1, 2, 3, 4, 5])

concatenated_products = dict()

upper_bound = 1000000

digits_sorted = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for test in range(2, upper_bound):
	n = 1
	product = ''
	list_of_ints = []
	while len(product) < 9:
		n += 1
		list_of_ints = list(range(1, n))
		product = concatenated_product(test, list_of_ints)
	if sorted(product) == digits_sorted:
		concatenated_products[(test, len(list_of_ints))] = int(product)

#print(concatenated_products)

max_key = miscmath.key_of_max_value(concatenated_products)

print(max_key, concatenated_products[max_key])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))