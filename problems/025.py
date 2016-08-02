import time

startTime = time.clock()

curr = 0
back2 = 1
back1 = 1
i = 2

while True:
	i += 1
	curr = back2 + back1
	back2 = back1
	back1 = curr
	if len(str(curr)) == 1000:
		break

print(i, curr)

endTime = time.clock()

print('Elapsed Time: ' + str(endTime - startTime))
