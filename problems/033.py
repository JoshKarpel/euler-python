import time
import miscmath

start_time = time.clock()

numerators = range(10, 100)
denominators = range(10, 100)
fractions = []

for numerator in numerators:
    for denominator in denominators:
        if denominator > numerator:
            fractions.append([numerator, denominator])

answers = []

for fraction in fractions:
    numerator_str = str(fraction[0])
    denominator_str = str(fraction[1])
    for i in numerator_str:
        if i == str(0):
            break
        elif i in denominator_str:
            numerator_str_cancelled = numerator_str.replace(i, '', 1)
            denominator_str_cancelled = denominator_str.replace(i, '', 1)
            # print(i, numerator_str, denominator_str, numerator_str_cancelled, denominator_str_cancelled)
            if denominator_str_cancelled != str(0) and int(numerator_str_cancelled) / int(denominator_str_cancelled) == fraction[0] / fraction[1]:
                answers.append(fraction[0] / fraction[1])
                print(fraction, fraction[0] / fraction[1], int(numerator_str_cancelled) / int(denominator_str_cancelled), numerator_str, denominator_str, numerator_str_cancelled, denominator_str_cancelled)

print(miscmath.list_product(answers))

print(answers)

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
