import time
import miscmath

start_time = time.clock()

upper_bound = 10000
iteration_bound = 50
lychrel = dict()

for test in range(1, upper_bound):
    iterations = 0
    initial = test
    lychrel[initial] = [test]
    while True:
        iterations += 1
        test += int(str(test)[::-1])
        lychrel[initial].append(test)
        if iterations > 50:
            break
        elif miscmath.is_palindrome(test):
            lychrel.pop(initial)
            break

print(lychrel)
print(len(lychrel))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
