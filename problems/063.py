import time

start_time = time.clock()


for n in range(1, 10):
    print(int('9' * n), 10 ** n)

nth_powers = [(i, j, i ** j, len(str(i ** j))) for j in range(1, 50) for i in range(2, 10)]
print(nth_powers)

total = 0
for i in nth_powers:
    if i[1] == i[3]:
        total += 1

print(total + 1)

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
