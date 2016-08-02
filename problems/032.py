import time
import miscmath

start_time = time.clock()

digits_sorted = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

permutations = miscmath.permutations(digits_sorted)

correct_products = set()

for digit_string in permutations:
    for i in range(1, 5):
        # print(int(''.join(digit_string[0:i])), int(''.join(digit_string[i:5])), int(''.join(digit_string[5:])))
        if int(''.join(digit_string[0:i])) * int(''.join(digit_string[i:5])) == int(''.join(digit_string[5:])):
            correct_products.add(int(''.join(digit_string[5:])))
            print(int(''.join(digit_string[0:i])), int(''.join(digit_string[i:5])), int(''.join(digit_string[5:])))

print(correct_products)
print(sum(correct_products))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
