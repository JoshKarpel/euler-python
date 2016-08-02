import time
import miscmath

start_time = time.clock()

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]
print(coin_values)


def count(combo):
    return sum(miscmath.elementwise_multiply(combo, coin_values))


# count = utils.Memoize(count)

def find_efficient_combo(target_value):
    combo = [0] * len(coin_values)
    for i in range(len(coin_values))[::-1]:
        while count(combo) <= target_value:
            combo[i] += 1
        combo[i] -= 1
    return combo


def find_efficient_combo_no_singles(target_value):
    combo = [0] * len(coin_values)
    for i in range(len(coin_values))[::-1]:
        if target_value < coin_values[i]:
            continue
        elif target_value == coin_values[i]:
            combo[i] = -1
            continue
        while count(combo) <= target_value:
            combo[i] += 1
        combo[i] -= 1
    return combo


divisions = [find_efficient_combo_no_singles(n) for n in coin_values]
print(divisions)

combination_count = 0

combo = find_efficient_combo(200)
final_combo = [200, 0, 0, 0, 0, 0, 0, 0]

iterator = range(len(combo))[::-1]


# while combo != final_combo:
#     for i in iterator:
#         while combo[i] > 0:
#             combo[i] -= 1
#             combo = miscmath.elementwise_sum(combo, divisions[i])
#             combination_count += 1
#             print(combo, combination_count)

def recursion(combo):
    combination_count = 0
    for i in iterator:
        subtracted = 0
        while combo[i] - subtracted > 0:
            print(combo)
            subtracted += 1
            combination_count += 1
            recursion(miscmath.elementwise_sum(combo, miscmath.elementwise_multiply([subtracted] * 8, divisions[i])))


recursion(combo)

print(combination_count)

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
