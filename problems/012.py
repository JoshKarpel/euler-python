import time
import miscmath

start_time = time.clock()

test = 500
triangle = 1

while True:
    test += 1
    # triangle += test
    triangle = int(test * (test + 1) / 2)
    # print(test,triangle,factors(triangle))
    if len(miscmath.full_factorization(triangle)) > 500:
        break

# print(test,triangle,factors(triangle))
print(test, triangle)

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
