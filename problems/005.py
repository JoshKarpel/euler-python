import time


def list_product(num_list):
    product = 1
    for i in num_list:
        product *= i
    return product


def find_answer():
    i = 20
    found = False
    while True:
        i += 1
        # if i > upperBound: break
        # if i%10000000 == 0: print(i/upperBound)
        for d in divisors:
            # print(i,d)
            if i % d != 0:
                found = False
                break
            found = True
        if found:
            return i


start_time = time.clock()

# upperBound = product([i for i in range(1,21)])
# print(upperBound)

divisors = range(2, 21)

print(find_answer())

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
