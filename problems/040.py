import time


start_time = time.clock()

champernowne = [str(i) for i in range(1, 1000000)]

champernowne = ''.join(champernowne)

print(int(champernowne[0]) * int(champernowne[9]) * int(champernowne[99]) * int(champernowne[999]) * int(champernowne[9999]) * int(champernowne[99999]) * int(champernowne[999999]))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))