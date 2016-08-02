import time
import miscmath


start_time = time.clock()

permutations = sorted(miscmath.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))

#print(permutations)

print(permutations[999999])

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))