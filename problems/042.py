import time


start_time = time.clock()

triangle_numbers = [n * (n + 1) / 2 for n in range(1,1000)]

file = open('042_words.txt', 'r')

word_value_list = [sum([(ord(i) - 96) for i in word]) for word in file.read().replace('"', '').lower().split(',')]

print(word_value_list)

print(len([i for i in word_value_list if i in triangle_numbers]))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))