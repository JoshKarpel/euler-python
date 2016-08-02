import time


def palindrome_test(n):
    reverse = ''
    n_str = str(n)
    for i in range(len(n_str)):
        reverse += n_str[-(i + 1)]
    if reverse == n_str:
        return True
    return False


start_time = time.clock()

products = []

for i in range(100, 1000):
    # print(i)
    for j in range(i, 1000):
        # print(i,j)
        # prod = i*j
        # if prod not in products: products.append(i*j)
        products.append(i * j)

# print('Products Done')

# print(products)
# print(sorted(products))

palindromes = [i for i in products if str(i) == str(i)[::-1]]

print(max(palindromes))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
